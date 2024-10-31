'''
The main idea of this file is to get data from various sources.
'''

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation, DataTransformationConfig

class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Entered data ingestion method or component')
        try:
            data = pd.read_csv(r'notebooks\data\StudentsPerformance.csv')
            logging.info('Data is read succesfully')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)

            data.to_csv(self.ingestion_config.train_data_path, index = False, header=True)
            logging.info('Data saved to train.csv')

            train_set, test_set = train_test_split(data, test_size = 0.2, random_state = 31)
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
            data.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)
            logging.info('Ingestion completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_trasformation = DataTransformation()
    data_trasformation.initiate_data_transformation(train_data, test_data)