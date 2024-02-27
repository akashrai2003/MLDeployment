import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    '''def __init__(self,config):
        self.config=config

    def __str__(self):
        return self.config

    def __repr__(self):
        return self.config
        
        
    instead of writing this we are skipping due to dataclass decorator'''

    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','data.csv')


class DataIngestion:
    '''
    A very professional way to write the code:

    def __init__(self,config:DataIngestionConfig):
        self.config=config
        self.logger=logging.getLogger(__name__)

    def read_data(self):
        try:
            self.logger.info("Reading raw data")
            self.raw_data=pd.read_csv(self.config.raw_data_path)
            self.logger.info("Raw data read successfully")
            return self.raw_data
        except Exception as e:
            self.logger.error(f"Error occured while reading raw data {str(e)}")
            raise CustomException(error_message=str(e),error_detail=sys.exc_info())

    def split_data(self):
        try:
            self.logger.info("Splitting raw data into train and test data")
            self.train_data,self.test_data=train_test_split(self.raw_data,test_size=0.2,random_state=42)
            self.logger.info("Data split successfully")
            return self.train_data,self.test_data
        except Exception as e:
            self.logger.error(f"Error occured while splitting data {str(e)}")
            raise CustomException(error_message=str(e),error_detail=sys.exc_info())

    def save_data(self):
        try:
            self.logger.info("Saving train and test data")
            self.train_data.to_csv(self.config.train_data_path,index=False)
            self.test_data.to_csv(self.config.test_data_path,index=False)
            self.logger.info("Data saved successfully")
        except Exception as e:
            self.logger.error(f"Error occured while saving data {str(e)}")
            raise CustomException(error_message=str(e),error_detail=sys.exc_info())

    def run(self):
        try:
            self.read_data()
            self.split_data()
            self.save_data()
        except CustomException as e:
            self.logger.error(f"Error occured while running data ingestion {str(e)}")
            raise CustomException(error_message=str(e),error_detail=sys.exc_info())
        except Exception as e:
            self.logger.error(f"Error occured while running data ingestion {str(e)}")
            raise CustomException(error_message=str(e),error_detail=sys.exc_info())
        else:
            self.logger.info("Data ingestion completed successfully")'''
    
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df=pd.read_csv(r'C:\Users\akash\Desktop\End to End ML\StudentPerformance\MLDeployment\Data\stud.csv')
            logging.info("Data read successfully")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initialized")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of Data completed successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            
            )
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()