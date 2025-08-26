# Image Captioning Model

This project implements an automatic image caption generation model (Image Captioning) using a deep learning architecture combining CNN and LSTM. The application is deployed via a Streamlit user interface that allows users to upload their own images and automatically generate text descriptions.

## Project Structure

```
.
├── main.py # Main Streamlit application
├── input_imgs/ # Folder to store input images
└── models/ # Folder containing trained models
├── feature_extractor.keras # CNN model for feature extraction
├── model.keras # Main model for caption generation
├── tokenizer.pkl # Tokenizer for text processing
└── flickr8k-image-captioning-using-cnns-and-lstms.ipynb # Training notebook
```

## Prerequisites

- Python 3.7+
- TensorFlow 2.x
- Streamlit
- Matplotlib
- NumPy
- Pickle

To install the Dependencies:

```bash
pip install tensorflow streamlit matplotlib numpy
```

## Features

1. **Interactive Web Interface**: User-friendly interface built with Streamlit
2. **Image Upload**: Ability to upload images in JPG, JPEG, or PNG formats
3. **Caption Generation**: Automatic generation of text descriptions for uploaded images
4. **Visualization**: Display the image with its generated caption

## How to Use the Application

1. Launch the application:
```bash
streamlit run main.py
```

2. Once the application is launched:
- Access the interface through your browser
- Click "Choose an image..." to upload an image
- The caption will be automatically generated and displayed below the image

## Technical Architecture

The project uses a two-part architecture:

1. **Feature Extractor** (CNN)
- Model Pre-trained to extract visual features from images
- Resizes images to 224x224 pixels
- Normalizes pixel values

2. Caption Generator (LSTM)
- Uses extracted features to generate a caption
- Generates the caption word by word sequentially
- Uses a tokenizer to convert words into numeric sequences

## Generation Workflow

1. Image Preprocessing:
- Loading and resizing
- Normalizing pixel values
- Extracting features using the CNN

2. Caption Generation:
- Initialization with "startseq"
- Sequential generation of words
- Stopping at "endseq" or maximum length reached

## Models and Training

The models were trained on the Flickr8k dataset, as documented in the notebook `flickr8k-image-captioning-using-cnns-and-lstms.ipynb`. Trained models are saved in the `models/` folder.

## Limitations

- Maximum sequence size: 34 words
- Still image size: 224x224 pixels
- Supported formats: JPG, JPEG, PNG

## Developer's note

Models are loaded with each prediction, which could be optimized for production deployment by keeping the models in memory.