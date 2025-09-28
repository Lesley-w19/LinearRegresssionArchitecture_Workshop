from sklearn.model_selection import train_test_split

class Preprocessing:
    @staticmethod
    def clean_data(data):
        # Implement data cleaning steps
        pass

    @staticmethod
    def normalize_data(data):
        # Implement data normalization steps
        pass

    @staticmethod
    def split_data(data, target_column, test_size=0.2):
        # Function to split data into training and testing sets
        X = data.drop(columns=[target_column])
        y = data[target_column]
        return train_test_split(X, y, test_size=test_size, random_state=42)
    
    def preprocess_data(self, data):
        # Function to preprocess data (e.g., handle missing values, feature scaling)
        if self.config['preprocessing']['fillna']:
            data = data.fillna(self.config['preprocessing']['fillna_value'])
        # Add more preprocessing steps as needed
        return data

   