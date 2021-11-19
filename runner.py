
from App_logging import logger
from Cassandra_python_Connection import connect_database
from src import load_data
import argparse

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    logger = logger.App_logger()
    args.add_argument('--config',default='params.yaml')
    parsed_args = args.parse_args()
    log_file = open("Overall_Log.txt", 'a+')
    #logger.log(log_file,"Started getting data from Cassandra...")
    #connect_database.connect_db().casandra_to_local_get_data(config_path=parsed_args.config)
    #logger.log(log_file,"Data from cassandra has been taken successfully...")
    #Get_data().get_data(config_path= parsed_args.config)
    logger.log(log_file,"Started getting data from given folder...")
    load_data.Load_data().load_and_save(config_path=parsed_args.config)
    logger.log(log_file,"Data from given folder has been Loaded & Saved successfully.......")
    log_file.close()
"""
import sys
sys.path.append(r'C:\Python_Lab\ineuron\internship\backorder\Back_Order_Prediction\App_logging')
sys.path.append(r'C:\Python_Lab\ineuron\internship\backorder\Back_Order_Prediction\Cassandra_python_Connection')
sys.path.append(r'C:\Python_Lab\ineuron\internship\backorder\Back_Order_Prediction\src')
import os
import argparse
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from connect_database import connect_db
from load_data import Load_data
from logger import App_logger

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    logger = App_logger()
    args.add_argument('--config',default='params.yaml')
    parsed_args = args.parse_args()
    log_file = open("Overall_Log.txt", 'a+')
    logger.log(log_file,"Started getting data from Cassandra...")
    connect_db().casandra_to_local_get_data(config_path=parsed_args.config)
    logger.log(log_file,"Data from cassandra has been taken successfully...")
    #Get_data().get_data(config_path= parsed_args.config)
    logger.log(log_file,"Started getting data from given folder...")
    Load_data().load_and_save(config_path=parsed_args.config)
    logger.log(log_file,"Data from given folder has been Loaded & Saved successfully.......")
    log_file.close()

"""