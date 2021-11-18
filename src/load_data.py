#read the data from data source 
#save it into data/raw for further process

import sys
sys.path.append(r'C:\Python_Lab\ineuron\internship\backorder\BackOrder_Prediction\App_logging')
sys.path.append(r'C:\Python_Lab\ineuron\internship\backorder\BackOrder_Prediction\python_project')
sys.path.append(r'C:\Python_Lab\ineuron\internship\backorder\BackOrder_Prediction\src')
import os
import argparse
from logger import App_logger
from connect_database import connect_db
from get_data import Get_data
import pandas as pd

class Load_data:
    def __init__(self):
        self.database = connect_db()
        self.fetched_data=Get_data()
        self.logger = App_logger()

    def load_and_save(self,config_path):
        config = self.database.read_params(config_path)
        log_file = open("Cassandra_Logs/saving_data_to_rawformatFolder_Log.txt", 'a+')
        #df = self.fetched_data.get_data(config_path)
        df = self.database.casandra_to_local_get_data(config_path)
        raw_data_path = config["load_data"]["raw_dataset_csv"]
        df.to_csv(raw_data_path,sep=",",index=False)
        self.logger.log(log_file,"Load data from remote sources and then saving it in data/raw folder")
        log_file.close()
        return df

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    parsed_args = args.parse_args()
    #connect_db().casandra_to_local_get_data(config_path=parsed_args.config)
    Load_data().load_and_save(config_path=parsed_args.config)

