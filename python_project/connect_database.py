import sys
sys.path.append(r'C:\Python_Lab\ineuron\internship\backorder\BackOrder_Prediction\App_logging')
sys.path.append(r'C:\Python_Lab\ineuron\internship\backorder\BackOrder_Prediction\src')
import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import pandas as pd
import yaml
import argparse
from datetime import datetime

from logger import App_logger


class connect_db:

    def __init__(self):
        self.logger = App_logger()

    def pandas_factory(self,colnames, rows):
        return pd.DataFrame(rows, columns=colnames)

    def read_params(self,config_path):
        with open(config_path) as yaml_file:
            config=yaml.safe_load(yaml_file)
        return config
    
    def casandra_to_local_get_data(self,config_path):
        log_file = open("Cassandra_Logs/accessing_data_from_cassandra_Log.txt", 'a+')
        config = self.read_params(config_path)
        self.logger.log(log_file, "Accessing cassandra connectivity...")
        secure_connect_bundles = config["cassandra_connectivity"]["secure_connect_bundle"]
        cloud_config= {'secure_connect_bundle': secure_connect_bundles}
        secure_connect_bundles = config["cassandra_connectivity"]["secure_connect_bundle"]
        ASTRA_CLIENT_ID = config["cassandra_connectivity"]["ASTRA_CLIENT_ID"]
        ASTRA_CLIENT_SECRET = config["cassandra_connectivity"]["ASTRA_CLIENT_SECRET"]
        auth_provider = PlainTextAuthProvider(ASTRA_CLIENT_ID,ASTRA_CLIENT_SECRET)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.logger.log(log_file, "Connecting cassandra db is done...")
        cassandra_DB_Name = config["data_sources"]["cassandra_DB_Name"]
        session = cluster.connect(cassandra_DB_Name)
        cassandra_Table_Name = config["data_sources"]["cassandra_Table_Name"]
        names=cassandra_Table_Name
        query = config["data_sources"]["query"]
        querys=query.format(names)
        session.row_factory = self.pandas_factory
        session.default_fetch_size = None
        rows = session.execute(querys)
        df = rows._current_rows
        self.logger.log(log_file, "Accessing rows from cassandra db is done...")
        casandra_to_local_path = config["data_sources"]["cassandra_to_local_path"]
        df.to_csv(casandra_to_local_path,index=False)
        self.logger.log(log_file, "Data has been successfully saved to given folder.")
        log_file.close()
        return df

"""
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    connect_db().casandra_to_local_get_data(config_path=parsed_args.config)

"""
