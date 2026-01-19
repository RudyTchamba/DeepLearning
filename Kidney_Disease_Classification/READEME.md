# Kidney Disease Classification MLFlow DVC Project

A deep learning project for kidney disease classification using Convolutional Neural Networks (CNN) with MLFlow for experiment tracking and DVC for data version control.

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Workflows](#workflows)
- [Installation](#installation)
- [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
- [Technologies Used](#technologies-used)
- [Project Workflows](#project-workflows)
- [Contributing](#contributing)

## 🔧 Prerequisites

Before you begin, ensure you have the following installed on your system:

### System Requirements
- **Python**: Version 3.8 or higher
- **pip**: Latest version (comes with Python)
- **Git**: For version control
- **Virtual Environment**: `venv` or `conda`

### Hardware Requirements
- **RAM**: Minimum 8GB (16GB recommended for training)
- **Storage**: At least 5GB free space
- **GPU**: Optional but recommended for faster training (CUDA-compatible)

### Operating System
- Linux (Ubuntu 18.04+)
- macOS (10.14+)
- Windows 10/11 with WSL2 (recommended)

## 📁 Project Structure

```
Kidney_Disease_Classification/
├── .github/
│   └── workflows/
│       └── .gitkeep
├── config/
│   └── config.yaml              # Configuration parameters
├── research/
│   └── trials.ipynb             # Experimental notebooks
├── src/
│   └── cnnClassifier/
│       ├── __init__.py
│       ├── components/          # Model components
│       ├── config/              # Configuration management
│       │   └── configuration.py
│       ├── constants/           # Project constants
│       ├── entity/              # Data entities
│       ├── pipeline/            # Training & prediction pipelines
│       └── utils/               # Utility functions
├── templates/
│   └── index.html               # Web interface templates
├── config.yaml                  # Main configuration file
├── dvc.yaml                     # DVC pipeline definition
├── params.yaml                  # Model hyperparameters
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup file
├── template.py                  # Project structure generator
└── README.md                    # Project documentation
```

## 🔀 Workflows

1. Update Config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py


## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/RudyTchamba/DeepLearning.git
cd DeepLearning/Kidney_Disease_Classification
```

### Step 2: Create a Virtual Environment

#### Using venv (Python's built-in)
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

#### Using conda (Alternative)
```bash
# Create conda environment
conda create -n kidney-disease python=3.10 -y

# Activate conda environment
conda activate kidney-disease
```

### Step 3: Install Dependencies

```bash
# Upgrade pip to latest version
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

**Note**: The `-e .` in `requirements.txt` installs the project package in editable mode.

## ⚙️ Setup Instructions

### 1. Initialize DVC (Data Version Control)

```bash
# Initialize DVC
dvc init

# Configure DVC remote storage (if applicable)
# dvc remote add -d storage <remote-url>
```

### 2. Configure MLFlow

MLFlow will be used for experiment tracking. No additional configuration needed for local runs.

### 3. Prepare Configuration Files

Edit the configuration files according to your setup:

- **`config/config.yaml`**: Set data paths, model parameters, and artifacts directory
- **`params.yaml`**: Define hyperparameters for model training
- **`dvc.yaml`**: Configure DVC pipeline stages

### 4. Download Dataset

Place your kidney disease dataset in the appropriate directory as specified in `config/config.yaml`.

```bash
# Example structure:
# artifacts/
# └── data_ingestion/
#     ├── train/
#     └── test/
```

## 🏃 Running the Project

### Option 1: Run Training Pipeline

```bash
# Execute the complete training pipeline
python main.py
```

### Option 2: Run with DVC Pipeline

```bash
# Run DVC pipeline (if configured in dvc.yaml)
dvc repro
```

### Option 3: Launch Web Application

```bash
# Start Flask web application
python app.py
```

The web interface will be available at `http://localhost:5000` (or the port specified in your app configuration).

### Option 4: Experiment in Jupyter Notebook

```bash
# Launch Jupyter Notebook
jupyter notebook

# Navigate to research/trials.ipynb
```

### Monitor Experiments with MLFlow

```bash
# Start MLFlow UI
mlflow ui

# Access at http://localhost:5000
```

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **TensorFlow** | Deep learning framework for CNN model |
| **MLFlow** | Experiment tracking and model registry |
| **DVC** | Data version control and pipeline management |
| **Flask** | Web application framework |
| **Pandas & NumPy** | Data manipulation and numerical operations |
| **Matplotlib & Seaborn** | Data visualization |
| **PyYAML** | Configuration file handling |
| **python-box** | Dictionary with attribute-style access |
| **gdown** | Google Drive file downloader |

## 📊 Project Workflows

### 1. Data Ingestion
- Download and extract dataset
- Organize data into train/test splits

### 2. Data Preparation
- Preprocess images
- Apply data augmentation
- Create data loaders

### 3. Model Training
- Build CNN architecture
- Train model with specified parameters
- Log metrics to MLFlow

### 4. Model Evaluation
- Evaluate on test set
- Generate performance metrics
- Visualize results

### 5. Model Deployment
- Save trained model
- Create prediction API
- Deploy web interface

## 🔍 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError`
```bash
# Solution: Ensure virtual environment is activated and dependencies are installed
pip install -r requirements.txt
```

**Issue**: TensorFlow GPU not detected
```bash
# Solution: Install CUDA and cuDNN compatible with your TensorFlow version
# Check compatibility: https://www.tensorflow.org/install/source#gpu
```

**Issue**: Permission denied errors
```bash
# Solution: Use appropriate permissions or run with sudo (not recommended for pip)
chmod +x script_name.py
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is part of a deep learning portfolio and is available for educational purposes.

## 👨‍💻 Author

**Rudy Tchamba**
- Email: rudyitiel@gmail.com
- GitHub: [@RudyTchamba](https://github.com/RudyTchamba)

## 🙏 Acknowledgments

- TensorFlow team for the deep learning framework
- MLFlow for experiment tracking capabilities
- DVC for data version control tools

---

**Note**: Make sure to update configuration files with your specific paths and parameters before running the project.