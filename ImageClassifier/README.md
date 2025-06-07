# Happy-Sad Image Classifier

## Project Overview
This project implements a deep learning model that classifies images of people as either "happy" or "sad". It includes both the model training pipeline and a web-based deployment interface using FastAPI.

## Directory Structure
```
ImageClassifier/
├── api.py              # FastAPI application for model deployment
├── notebook_model.ipynb # Jupyter notebook containing model development
├── requirements.txt    # Project dependencies
├── script.py           # Utility script for image collection
├── data/              # Training and validation data
│   ├── happy/         # Images of happy people
│   └── sad/           # Images of sad people
├── logs/              # Training and validation logs
│   ├── train/
│   └── validation/
├── models/            # Saved model files
│   └── happy_sad_model.h5
├── static/           # Static files for web interface
└── templates/        # HTML templates
    └── index.html    # Main web interface template
```

## Features
- Deep Learning image classification using TensorFlow/Keras
- Binary classification (happy/sad)
- Interactive web interface for real-time predictions
- RESTful API endpoints for model integration
- Drag-and-drop image upload
- Real-time predictions with confidence scores
- Responsive design using Tailwind CSS

## Technical Stack
- **Backend Framework**: FastAPI
- **Deep Learning**: TensorFlow/Keras
- **Image Processing**: OpenCV, Pillow
- **Frontend**: HTML5, JavaScript, Tailwind CSS
- **Development Tools**: Jupyter Notebook
- **Deployment**: Uvicorn ASGI server

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ImageClassifier
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Training the Model
The model training process is documented in `notebook_model.ipynb`. You can rerun the training by:
1. Opening the notebook in Jupyter
2. Running all cells sequentially
3. The trained model will be saved in `models/happy_sad_model.h5`

### Running the Web Application

1. Start the FastAPI server:
```bash
uvicorn api:app --reload
```

2. Open your browser and navigate to:
```
http://localhost:8000
```

## API Endpoints

### 1. Web Interface
- **URL**: `/`
- **Method**: GET
- **Description**: Returns the main web interface for image upload and classification

### 2. Prediction Endpoint
- **URL**: `/predict`
- **Method**: POST
- **Input**: Form data with image file
- **Returns**: JSON with prediction results
```json
{
    "label": "happy/sad",
    "confidence": 0.95,
    "probability_happy": 0.95
}
```

## Model Architecture
The image classification model is built using TensorFlow/Keras and includes:
- Input preprocessing to 256x256 RGB images
- Convolutional Neural Network (CNN) layers
- Binary classification output
- Training with categorical crossentropy loss

## Development

### Adding New Features
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

### Code Style
- Follow PEP 8 guidelines for Python code
- Use type hints where possible
- Document new functions and classes

## Data Collection
The project includes a data collection script (`script.py`) that can be used to gather additional training images. The script:
- Scrapes images from web searches
- Automatically downloads and organizes images
- Supports multiple image formats (JPEG, PNG, etc.)

## Production Deployment
For production deployment:
1. Use a production-grade ASGI server
2. Set up proper security measures
3. Configure CORS policies
4. Use environment variables for sensitive data

```bash
# Example production deployment
gunicorn -w 4 -k uvicorn.workers.UvicornWorker api:app
```

## Contributing
Contributions are welcome! Please read the contributing guidelines before submitting pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- TensorFlow team for the deep learning framework
- FastAPI team for the excellent web framework
- Contributors to the training dataset

## Contact
For questions and support, please open an issue in the repository.

## Future Improvements
- [ ] Add support for multiple image classification
- [ ] Implement model versioning
- [ ] Add user authentication
- [ ] Improve prediction speed
- [ ] Add batch processing capability
- [ ] Implement model retraining API
- [ ] Add more detailed analytics
