import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd 

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


#to perfrom data ingestion there need an input for example like path for storing raw data, trained data etc
# therefore we will make a class which we can use for all input

@dataclass
class DataIngestionConfig:
    #trained data or output will be stored in path (artifacts folder in mentioned file)
    train_data_path: str=os.path.join("artifacts","train.csv")
    test_data_path: str=os.path.join("artifacts","test.csv")
    raw_data_path: str=os.path.join("artifacts","data.csv")
    
    #this can be defined in another folder called config_entity but for simplicity its defined here

class DataIngestion:
    #if we are only defining variable we can use dataclass but if we are defining a function inside then
    # we should use init fn 
    def __init__(self):
        # all 3 paths of dataingestion config will be stored in below variable
        self.ingestion_config=DataIngestionConfig() 
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            #reading dataset
            df=pd.read_csv("C:/Users/M/Juypter/E2E project/src/notebook/data/stud.csv") # here the source can be Mysql or mongodb etc
            logging.info("Read the dataset as Dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            #converting raw to csv file
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")

            # performing train test split
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            #saving train set and test set 
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                #this will return train data path and test data path 
                #to next step which is data transformation 
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()