from sklearn.linear_model import LinearRegression

class linear_regression_model:
    def __init__(self):
        self.model = LinearRegression()

    def get_features_and_target_train(self, data):
        # Function to separate features and target variable
        X = data[self.config['features']['selected']]
        y = data[self.config['data']['target']]
        return X, y

    def get_features_and_target_test(self, data):
        # Function to separate features and target variable for test data
        X = data[self.config['features']['selected']]
        y = data[self.config['data']['target']]
        return X, y