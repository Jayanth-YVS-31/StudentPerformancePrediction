import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
import dill

class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        try:
            numerical_columns = ['writing score', 'reading score']
            categorical_columns = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']

            num_pipeline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler(with_mean= False))
                ]
            )
            cat_pipeline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('onehot', OneHotEncoder(handle_unknown='ignore')),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )

            logging.info('numerical and categorical column completed')

            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, numerical_columns),
                    ('cat_pipeline', cat_pipeline, categorical_columns)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            logging.info('Read train and test data completed')

            logging.info('Obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = 'math score'
            numerical_columns = ['writing score', 'reading score']


            # Drop target column to get input features for both train and test
            input_feature_train_data = train_data.drop(columns=[target_column_name], axis=1)
            input_feature_test_data = test_data.drop(columns=[target_column_name], axis=1)
            
            # Extract target features for both train and test
            target_feature_train_data = train_data[target_column_name]
            target_feature_test_data = test_data[target_column_name]

            logging.info('Applying preprocessing object on training and testing dataframes')

            # Apply preprocessing object on training and testing input features
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_data)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_data)

            # Concatenate processed input features with target features for train and test
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_data)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_data)]

            logging.info('Saved preprocessing object')

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e, sys)