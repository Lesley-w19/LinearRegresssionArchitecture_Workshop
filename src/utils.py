import psycopg2
import yaml
import pandas as pd


class Utils:
    def __init__(self, config_path):
        self.config_path = config_path

    # load configuration from yaml file
    def load_config(config_path):
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config

    # connect to the database
    def create_db_connection(self):
        conn_str = self.config['connection']

        try:
            conn = psycopg2.connect(conn_str)
            print("Database connection successful")
            return conn
        
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return None
        
    def close_db_connection(conn):
        conn.close()

    

conn_instance = Utils.load_config('./configs/config.yaml')
print(conn_instance)