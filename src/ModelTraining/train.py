    
from pyexpat import model
from src.ModelSelection.model import linear_regression_model
import joblib

class ModelTrainer:
    def __init__(self):
        self.model = linear_regression_model()

    def train(self, X_train, y_train):
        self.model.train(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)
    def train_model(self, train_data, epochs=100, batch_size=32, checkpoint_dir=None):
        # Function to train the model
        X_train, y_train = train_data.drop(columns=['target']), train_data['target']
        self.model.train(X_train, y_train)

        if checkpoint_dir:
            joblib.dump(self.model, f"{checkpoint_dir}/model_checkpoint.pkl")

        return self.model