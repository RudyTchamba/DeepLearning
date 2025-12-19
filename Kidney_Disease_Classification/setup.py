import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPOSITORY_URL = "https://github.com/RudyTchamba/DeepLearning/tree/main/Kidney_Disease_Classification"
AUTHOR_USER_NAME ="RudyTchamba"
SRC_REPO = "cnnClassifier",
AUTHOR_EMAIL = "rudyitiel@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Convolutional Neural Network (CNN) based classifier for kidney disease detection.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=REPOSITORY_URL,
    project_urls={
        "Bug Tracker": f"{REPOSITORY_URL}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)