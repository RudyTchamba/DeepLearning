# 🤖 Chatbot Service Client Pikart

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-green.svg)
![Flask](https://img.shields.io/badge/flask-2.3%2B-red.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

Une application de chatbot intelligent et moderne construite avec Flask, TensorFlow, et une interface web magnifique et responsive. Système de service client entièrement automatisé pour Pikart.

## 📋 Table des matières

- [À propos](#à-propos)
- [Caractéristiques](#caractéristiques)
- [Prérequis](#prérequis)
- [Installation](#installation)
  - [Clonage du repository](#clonage-du-repository)
  - [Configuration de l'environnement](#configuration-de-lenvironnement)
  - [Installation des dépendances](#installation-des-dépendances)
- [Structure du projet](#structure-du-projet)
- [Utilisation](#utilisation)
  - [Démarrage de l'application](#démarrage-de-lapplication)
  - [Accès à l'interface](#accès-à-linterface)
- [Architecture](#architecture)
- [API Documentation](#api-documentation)
- [Technologies](#technologies)
- [Configuration avancée](#configuration-avancée)
- [Dépannage](#dépannage)
- [Contribuer](#contribuer)

## À propos

Le **Chatbot Service Client Pikart** est une solution complète d'assistant conversationnel basée sur l'intelligence artificielle. Il utilise un modèle de réseau de neurones entraîné sur des intentions de service client pour fournir des réponses rapides et précises aux clients.

### Cas d'usage

- ✅ Support client 24/7
- ✅ Réponses automatisées aux questions fréquentes
- ✅ Guidance des utilisateurs
- ✅ Collecte d'informations
- ✅ Escalade intelligente vers des agents humains

## ✨ Caractéristiques

### Frontend
- 🎨 **Interface magnifique** - Design moderne avec thème sombre élégant
- 📱 **Responsive Design** - Fonctionne parfaitement sur mobile, tablette et desktop
- ✨ **Animations fluides** - Transitions et animations élégantes
- 😊 **Sélecteur d'emojis** - Enrichir les messages avec des emojis
- 💾 **Historique persistant** - Sauvegarde locale de la conversation
- ⌨️ **Raccourcis clavier** - Navigation optimisée au clavier
- 🔔 **Notifications** - Toast notifications pour les actions

### Backend
- 🧠 **Modèle IA** - Réseau de neurones TensorFlow pré-entraîné
- 🎯 **Traitement NLP** - NLTK pour tokenization et lemmatization
- 🔄 **Réponses contextuelles** - Réponses basées sur les intents
- 📊 **Scoring de confiance** - Filtre les prédictions de faible confiance
- 🚀 **Performance** - Réponses instantanées

## 🔧 Prérequis

Avant de commencer, assurez-vous d'avoir installé:

- **Python 3.8** ou supérieur
  ```bash
  python3 --version  # Vérifier la version
  ```
- **pip** (gestionnaire de paquets Python)
  ```bash
  pip3 --version  # Vérifier l'installation
  ```
- **Git** (pour cloner le repository)
  ```bash
  git --version  # Vérifier l'installation
  ```

### Système d'exploitation supporté

- ✅ Linux (Ubuntu, Debian, Fedora, etc.)
- ✅ macOS (10.14+)
- ✅ Windows 10/11 (WSL2 recommandé)

## 📦 Installation

### Clonage du repository

```bash
# Cloner le projet
git clone https://github.com/RudyTchamba/DeepLearning/tree/main/ChatBot_using_NLTK

# Accéder au répertoire du projet
cd chatbot-pikart
```

### Configuration de l'environnement

#### Option 1: Utiliser un environnement virtuel (Recommandé)

```bash
# Créer un environnement virtuel Python
python3 -m venv venv

# Activer l'environnement virtuel

# Sur Linux/macOS:
source venv/bin/activate

# Sur Windows (CMD):
venv\Scripts\activate

# Sur Windows (PowerShell):
venv\Scripts\Activate.ps1
```

#### Option 2: Utiliser Conda

```bash
# Créer un environnement Conda
conda create -n pikart-chatbot python=3.10

# Activer l'environnement
conda activate pikart-chatbot
```

### Installation des dépendances

```bash
# Mettre à jour pip
pip install --upgrade pip setuptools wheel

# Installer toutes les dépendances
pip install -r requirements.txt
```

**Note:** L'installation peut prendre quelques minutes en raison des dépendances volumineuses (TensorFlow).

#### Vérification de l'installation

```bash
# Vérifier que tous les paquets sont correctement installés
python3 -c "
import flask, tensorflow, nltk, sklearn
print('✓ Flask:', flask.__version__)
print('✓ TensorFlow:', tensorflow.__version__)
print('✓ NLTK:', nltk.__version__)
print('✓ Sklearn:', sklearn.__version__)
print('✓ Installation réussie!')
"
```

## 📁 Structure du projet

```
chatbot-pikart/
│
├── 📄 app.py                              # Application Flask principale
├── 📄 requirements.txt                    # Dépendances Python
├── 📄 README.md                           # Ce fichier
├── 📄 intents.json                        # Définition des intents et réponses
│
├── 🤖 Modèles (fichiers pré-entraînés)
│   ├── chatbot_model.h5                   # Modèle Neural Network
│   ├── words.pkl                          # Vocabulaire encodé
│   └── classes.pkl                        # Classes d'intents
│
├── 📓 Notebooks
│   └── Pikart_customer_service_chatbot.ipynb  # Notebook d'entraînement
│
├── 🎨 Templates (Frontend HTML)
│   └── templates/
│       └── index.html                     # Interface web
│
└── 🎨 Fichiers statiques
    └── static/
        ├── css/
        │   └── style.css                  # Styles CSS (animations, thème)
        └── js/
            └── script.js                  # Logique JavaScript (interactions)
```

## 🚀 Utilisation

### Démarrage de l'application

```bash
# S'assurer que l'environnement virtuel est activé
# (voir Configuration de l'environnement ci-dessus)

# Lancer l'application Flask
python3 app.py
```

**Sortie attendue:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Accès à l'interface

1. Ouvrez votre navigateur web
2. Allez à: **http://localhost:5000**
3. Commencez à converser avec le chatbot! 💬

## 🏗️ Architecture

### Architecture système

```
┌─────────────────────────────────────────────────┐
│           Frontend (Interface Web)              │
│  HTML5 | CSS3 (Animations) | JavaScript (Vanilla)│
│                                                 │
│  • Messages en temps réel                       │
│  • Interface responsive                         │
│  • Sauvegarde locale (LocalStorage)            │
└──────────────────┬──────────────────────────────┘
                   │ HTTP POST
                   │ (/chat_response)
                   ▼
┌─────────────────────────────────────────────────┐
│    Backend (Flask + TensorFlow)                │
│                                                 │
│  Flask Application                              │
│  ├── Routes HTTP                                │
│  └── Logique de traitement                      │
│                                                 │
│  Pipeline de traitement:                        │
│  1. Tokenization (NLTK)                        │
│  2. Lemmatization (NLTK)                       │
│  3. Bag of Words                               │
│  4. Prédiction (Neural Network TensorFlow)     │
│  5. Sélection de réponse                       │
└──────────────────┬──────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────┐
│    Base de données (intents.json)              │
│                                                 │
│  • Tags d'intentions                            │
│  • Patterns (entrées utilisateur)              │
│  • Réponses pré-définies                       │
└─────────────────────────────────────────────────┘
```

### Flux de traitement d'un message

```
Message utilisateur
        │
        ▼
   Tokenization (NLTK: word_tokenize)
        │
        ▼
   Lemmatization (NLTK: WordNetLemmatizer)
        │
        ▼
   Bag of Words (Encodage numérique)
        │
        ▼
   Neural Network Prediction (TensorFlow)
        │
        ▼
   Filtrage par seuil (ERROR_THRESHOLD = 0.25)
        │
        ▼
   Sélection du meilleur intent
        │
        ▼
   Récupération de la réponse (intents.json)
        │
        ▼
   Réponse JSON → Frontend
```

## 📡 API Documentation

### Endpoints disponibles

#### 1. GET /
Récupère la page principale du chatbot

**Réponse:** Page HTML interactive

```bash
curl http://localhost:5000/
```

#### 2. POST /chat_response
Envoie un message et reçoit une réponse du chatbot

**URL:** `http://localhost:5000/chat_response`

**Méthode:** POST

**Headers:**
```json
{
  "Content-Type": "application/json"
}
```

**Corps de la requête:**
```json
{
  "message": "Bonjour, comment puis-je vous aider?"
}
```

**Réponse (200 OK):**
```json
{
  "response": "Bonjour! Bienvenue chez Pikart. Comment puis-je vous assister aujourd'hui?"
}
```

**Exemple avec cURL:**
```bash
curl -X POST http://localhost:5000/chat_response \
  -H "Content-Type: application/json" \
  -d '{"message": "Bonjour"}'
```

**Exemple avec Python:**
```python
import requests

url = 'http://localhost:5000/chat_response'
payload = {'message': 'Bonjour'}
response = requests.post(url, json=payload)
print(response.json())  # {'response': '...'}
```

**Exemple avec JavaScript:**
```javascript
fetch('/chat_response', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ message: 'Bonjour' })
})
.then(response => response.json())
.then(data => console.log(data.response))
.catch(error => console.error('Error:', error));
```

## 💻 Technologies

### Backend
| Technologie | Version | Description |
|-------------|---------|-------------|
| **Flask** | 2.3+ | Framework web Python |
| **TensorFlow** | 2.13+ | Framework ML/IA |
| **NLTK** | 3.8+ | Traitement du langage naturel |
| **scikit-learn** | 1.3+ | Machine learning |
| **NumPy** | 1.24+ | Calcul scientifique |
| **Pickle** | - | Sérialisation de données |

### Frontend
| Technologie | Description |
|-------------|-------------|
| **HTML5** | Structure sémantique |
| **CSS3** | Styling avec animations fluides |
| **JavaScript (Vanilla)** | Interactivité sans frameworks |
| **Font Awesome 6** | Icônes modernes |
| **Google Fonts** | Typographie (Poppins, Inter) |

### Outils de développement
- **Git** - Contrôle de version
- **pip** - Gestionnaire de paquets Python
- **Virtual Environment** - Isolation d'environnement

## ⚙️ Configuration avancée

### Variables d'environnement

Créez un fichier `.env` à la racine du projet:

```bash
# Mode de debug
FLASK_ENV=development
FLASK_DEBUG=True

# Configuration Flask
FLASK_APP=app.py
FLASK_PORT=5000

# Configuration du modèle
MODEL_PATH=chatbot_model.h5
INTENTS_PATH=intents.json
ERROR_THRESHOLD=0.25
```

### Charger les variables d'environnement

```bash
# Installer python-dotenv (si pas déjà fait)
pip install python-dotenv

# Dans app.py, ajouter au début:
from dotenv import load_dotenv
load_dotenv()
```

### Personnalisation du modèle

Pour réentraîner le modèle avec vos propres intentions:

1. Modifiez `intents.json` avec vos patterns et réponses
2. Ouvrez `Pikart_customer_service_chatbot.ipynb` dans Jupyter
3. Exécutez les cellules pour réentraîner le modèle
4. Le modèle sera sauvegardé dans `chatbot_model.h5`

```bash
# Lancer Jupyter Notebook
jupyter notebook Pikart_customer_service_chatbot.ipynb
```

### Performance

Pour améliorer les performances:

```python
# Dans app.py, charger le modèle une seule fois
chat_model = load_model('chatbot_model.h5')

# Utiliser eager execution pour TensorFlow (plus rapide)
import tensorflow as tf
tf.config.run_functions_eagerly(True)
```

## 🐛 Dépannage

### Erreur: "ModuleNotFoundError: No module named 'flask'"

**Solution:** L'environnement virtuel n'est pas activé

```bash
# Activer l'environnement virtuel
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows
```

### Erreur: "ValueError: numpy.dtype size changed"

**Solution:** Incompatibilité de versions NumPy/scikit-learn

```bash
# Réinstaller les dépendances
pip uninstall -y numpy scikit-learn
pip install --upgrade -r requirements.txt
```

### Erreur: "FileNotFoundError: [Errno 2] No such file or directory: 'intents.json'"

**Solution:** Vérifier que vous êtes dans le bon répertoire

```bash
# Vérifier les fichiers présents
ls -la

# S'assurer d'être dans le répertoire du projet
pwd
cd /chemin/vers/chatbot-pikart
```

### Erreur: "Port 5000 déjà en utilisation"

**Solution:** Utiliser un port différent

```bash
# Linux/macOS - Terminer le processus
lsof -ti:5000 | xargs kill -9

# Windows - Utiliser un autre port dans app.py
app.run(debug=True, port=5001)
```

### Le chatbot ne répond pas correctement

**Causes possibles et solutions:**

1. **intents.json invalide** - Vérifier la validité du JSON
   ```bash
   python3 -m json.tool intents.json
   ```

2. **Modèle pas trouvé** - Vérifier que `chatbot_model.h5` existe
   ```bash
   ls -lh *.h5 *.pkl
   ```

3. **Seuil de confiance trop élevé** - Modifier `ERROR_THRESHOLD` dans app.py

4. **Intentions insuffisantes** - Réentraîner le modèle avec plus de patterns

### Application très lente

**Solutions:**

1. Augmenter les ressources CPU/RAM
2. Optimiser la taille du modèle
3. Utiliser GPU (CUDA) pour TensorFlow
4. Implémenter du caching pour les réponses fréquentes

### Interface web ne charge pas

**Solutions:**

1. Vérifier que Flask écoute sur le bon port
2. Nettoyer le cache du navigateur (Ctrl+Shift+Del)
3. Vérifier la console du navigateur (F12) pour les erreurs
4. Vérifier les fichiers statiques (`css/style.css`, `js/script.js`)

## 📚 Ressources supplémentaires

- [Documentation Flask](https://flask.palletsprojects.com/)
- [Documentation TensorFlow](https://www.tensorflow.org/)
- [Documentation NLTK](https://www.nltk.org/)
- [Documentation scikit-learn](https://scikit-learn.org/)

## 🤝 Contribuer

Les contributions sont bienvenues! Pour contribuer:

1. **Forkez** le repository
2. **Créez une branche** pour votre feature (`git checkout -b feature/AmazingFeature`)
3. **Commitez vos changements** (`git commit -m 'Add AmazingFeature'`)
4. **Pushez la branche** (`git push origin feature/AmazingFeature`)
5. **Ouvrez une Pull Request**

### Directives de contribution

- Respecter le style de code existant
- Tester avant de soumettre
- Documenter les changements
- Mettre à jour le README si nécessaire

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

**Pikart Team**
- Site web: [pikart.com](https://pikart.com)
- Email: support@pikart.com

## 🙏 Remerciements

- TensorFlow et Keras pour l'infrastructure ML
- NLTK pour le traitement du langage naturel
- Flask pour le framework web
- Font Awesome pour les icônes

## 📞 Support et contact

### Pour les questions ou problèmes:

- 📧 Email: support@pikart.com
- 🐛 Issues: [GitHub Issues](https://github.com/pikart/chatbot/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/pikart/chatbot/discussions)

## 🗺️ Roadmap

- [ ] Support multilingue (EN, ES, DE, IT)
- [ ] Intégration avec bases de données
- [ ] Dashboard d'analytics
- [ ] API REST complète
- [ ] Webhooks pour intégrations tierces
- [ ] Support des images et fichiers
- [ ] Système de files d'attente pour escalade
- [ ] Authentification des utilisateurs
- [ ] Tests automatisés

---

<div align="center">

**[⬆ Retour au sommet](#-chatbot-service-client-pikart)**

Fait avec ❤️ par l'équipe Pikart

</div>
