## read params
## process 
## return data frame
import sys
sys.path.append(r'C:\Python_Lab\ineuron\internship\backorder\BackOrder_Prediction\App_logging')
sys.path.append(r'C:\Python_Lab\ineuron\internship\backorder\BackOrder_Prediction\python_project')
import os
import yaml
import pandas as pd
import argparse
from connect_database import connect_db
from logger import App_logger

class Get_data:
    def __init__(self):
        self.database = connect_db()
        self.logger = App_logger()
    
    def get_data(self,config_path):
        config = self.database.read_params(config_path)
        log_file = open("Cassandra_Logs/accessing_data_from_folder_Log.txt", 'a+')
        self.logger.log(log_file,"Started getting data from given folder...")
        data_path = config["data_sources"]["cassandra_to_local_path"]
        df = pd.read_csv(data_path,sep=",",encoding='utf-8',low_memory=False)
        self.logger.log(log_file,"Data has been successfully readed from the given folder.")
        log_file.close()
        return df
    
"""
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    #connect_db().casandra_to_local_data(config_path=parsed_args.config)
    Get_data().get_data(config_path= parsed_args.config)
"""

"""
logging_str = "[%(asctime)s: %(levelname)s: %(module)s:] %(message)s"
log_dir = "logs"
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(filename=os.path.join(log_dir,"running.log"),
                                            level=logging.INFO,
                                format=logging_str,
                                filemode='a',
                                datefmt = "%Y-%m-%d %H:%M:%S")

logging.info("Started with Stage 1")
"""