import numpy as np
import pandas as pd
import sklearn
from sklearn.metrics import mean_squared_error, r2_score

class ModelEvaluator:
    def __init__(self, model):
        self.model = model
        
    def regresion_metrics(y_true, y_pred):
    # Function to calculate regression metrics
        mse = np.mean((y_true - y_pred) ** 2)
        rmse = np.sqrt(mse)
        mae = np.mean(np.abs(y_true - y_pred))
        return {'MSE': mse, 'RMSE': rmse, 'MAE': mae}

    def evaluate(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        return self.regresion_metrics(y_test, y_pred)
    
    
    

