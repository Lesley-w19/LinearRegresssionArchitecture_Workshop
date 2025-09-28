import pandas as pd
from src.utils import Utils

class DataLoader:
    def __init__(self, config):
        self.config = config

    def load_data(self):
        # Function to load data based on the provided configuration
        return pd.read_csv(self.config['data']['path'])

    # load from database
    def load_data_from_db(self, query):
        import sqlite3
        conn = sqlite3.connect(self.config['data']['db_path'])
        return pd.read_sql_query(query, conn)
    

    def save_processed_data(self, data, path):
        # Function to save processed data to a specified path
        data.to_csv(path, index=False)
        

    def load_processed_data(self, path):
        # Function to load processed data from a specified path
        return pd.read_csv(path)


