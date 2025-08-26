import streamlit as st
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import tensorflow as tf
import pickle
import matplotlib.pyplot as plt
import numpy as np
import os

# Caption generator function with error handling
def generate_and_display_caption(image_path, model_path, tokenizer_path, feature_extractor_path, max_length=34, img_size=224):
    try:
        # Load the trained models and tokenizer with error handling
        st.write("🔄 Chargement des modèles...")
        
        # Try different loading methods for compatibility
        try:
            caption_model = tf.keras.models.load_model(model_path, compile=False)
            st.write("✅ Modèle de caption chargé avec succès")
        except Exception as e:
            st.error(f"❌ Erreur lors du chargement du modèle de caption: {str(e)}")
            st.error("Essayez de re-sauvegarder votre modèle avec la version actuelle de Keras")
            return
        
        try:
            feature_extractor = tf.keras.models.load_model(feature_extractor_path, compile=False)
            st.write("✅ Extracteur de caractéristiques chargé avec succès")
        except Exception as e:
            st.error(f"❌ Erreur lors du chargement de l'extracteur: {str(e)}")
            return

        # Load tokenizer
        try:
            with open(tokenizer_path, "rb") as f:
                tokenizer = pickle.load(f)
            st.write("✅ Tokenizer chargé avec succès")
        except Exception as e:
            st.error(f"❌ Erreur lors du chargement du tokenizer: {str(e)}")
            return

        # Preprocess the image
        st.write("🖼️ Traitement de l'image...")
        img = load_img(image_path, target_size=(img_size, img_size))
        img = img_to_array(img) / 255.0  # Normalize pixel values
        img = np.expand_dims(img, axis=0)
        
        # Extract image features
        image_features = feature_extractor.predict(img, verbose=0)
        st.write("✅ Caractéristiques de l'image extraites")
        
        # Generate the caption
        st.write("🤖 Génération du caption...")
        in_text = "startseq"
        for i in range(max_length):
            sequence = tokenizer.texts_to_sequences([in_text])[0]
            sequence = pad_sequences([sequence], maxlen=max_length)
            yhat = caption_model.predict([image_features, sequence], verbose=0)
            yhat_index = np.argmax(yhat)
            word = tokenizer.index_word.get(yhat_index, None)
            if word is None:
                break
            in_text += " " + word
            if word == "endseq":
                break
        
        caption = in_text.replace("startseq", "").replace("endseq", "").strip()
        st.write("✅ Caption généré avec succès")

        # Display the image with the generated caption
        img_display = load_img(image_path, target_size=(img_size, img_size))
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.imshow(img_display)
        ax.axis('off')
        ax.set_title(caption, fontsize=14, color='blue', wrap=True, pad=20)
        st.pyplot(fig)
        
        # Display the caption as text with better formatting
        st.markdown("### 💬 Caption Généré:")
        st.success(f"**{caption}**")
        
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
        st.error("Please check your model files and try again.")

def check_model_files(model_path, tokenizer_path, feature_extractor_path):
    """Check if all required model files exist"""
    missing_files = []
    
    if not os.path.exists(model_path):
        missing_files.append(model_path)
    if not os.path.exists(tokenizer_path):
        missing_files.append(tokenizer_path)
    if not os.path.exists(feature_extractor_path):
        missing_files.append(feature_extractor_path)
    
    return missing_files

def main():
    st.title('🖼️ Générateur de Captions d\'Images')
    st.write('Uploadez une image pour générer une description automatique avec l\'intelligence artificielle.')
    
    # Model file paths
    model_path = "models/model.keras"
    tokenizer_path = "models/tokenizer.pkl"
    feature_extractor_path = "models/feature_extractor.keras"
    
    # Check if model files exist
    missing_files = check_model_files(model_path, tokenizer_path, feature_extractor_path)
    
    if missing_files:
        st.error("⚠️ Fichiers de modèle manquants:")
        for file in missing_files:
            st.error(f"- {file}")
        st.error("Veuillez vous assurer que tous les fichiers de modèle sont dans le bon répertoire.")
        return
    
    # Display system information
    with st.expander("ℹ️ Informations Système"):
        st.write(f"Version TensorFlow: {tf.__version__}")
        st.write(f"Version Keras: {tf.keras.__version__}")
    
    # Upload an image
    uploaded_image = st.file_uploader(
        "📁 Choisissez une image...", 
        type=["jpg", "jpeg", "png"],
        help="Uploadez une image JPG, JPEG, ou PNG"
    )

    if uploaded_image is not None:
        # Save image temporarily
        temp_image_path = "temp.jpg"
        with open(temp_image_path, "wb") as f:
            f.write(uploaded_image.getbuffer())

        # Create two columns layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📤 Image Uploadée")
            st.image(uploaded_image, caption="Image Originale", use_column_width=True)
        
        with col2:
            st.subheader("🤖 Résultat avec Caption")
            # Placeholder for the result
            result_placeholder = st.empty()

        # Generate caption with a button (centered)
        st.markdown("<br>", unsafe_allow_html=True)
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
        with col_btn2:
            if st.button("🚀 Générer Caption", type="primary", use_container_width=True):
                with st.spinner("Génération du caption en cours..."):
                    # Generate caption and display in right column
                    with col2:
                        generate_and_display_caption(
                            temp_image_path, 
                            model_path, 
                            tokenizer_path, 
                            feature_extractor_path
                        )
        
        # Clean up temporary file
        if os.path.exists(temp_image_path):
            try:
                os.remove(temp_image_path)
            except:
                pass  # Ignore cleanup errors

    # Add instructions
    st.markdown("---")
    with st.expander("📋 Instructions d'utilisation"):
        st.markdown("""
        1. **Uploadez une image** en utilisant le sélecteur de fichier ci-dessus
        2. **Cliquez sur le bouton "Générer Caption"** 
        3. **Attendez** que le modèle traite et génère une description
        4. **Visualisez le résultat** dans la colonne de droite
        
        **Formats supportés:** JPG, JPEG, PNG  
        **Taille maximum:** 200MB par fichier
        """)
    
    # Add footer
    st.markdown("---")
    st.markdown("*Développé avec ❤️ en utilisant Streamlit et TensorFlow*")

if __name__ == "__main__":
    main()