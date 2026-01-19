import os
import gdown
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self)-> str:
        """Downloads file from Google Drive using gdown."""
        
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from : {dataset_url} into to : {zip_download_dir}")
            
            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + file_id, str(zip_download_dir), quiet=False)
            
            logger.info(f"Downloaded data from : {dataset_url} into file : {zip_download_dir}")
        
        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        """Extracts the downloaded zip file."""
        
        try:
            unzip_dir = self.config.unzip_dir
            zip_file_path = self.config.local_data_file
            
            logger.info(f"Extracting zip file: {zip_file_path} into dir: {unzip_dir}")
            
            with zipfile.ZipFile(str(zip_file_path), 'r') as zip_ref:
                zip_ref.extractall(str(unzip_dir))
            
            logger.info(f"Extracted zip file: {zip_file_path} into dir: {unzip_dir}")
        
        except Exception as e:
            raise e