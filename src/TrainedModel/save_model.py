class ModelSaver:
    def __init__(self, model, path):
        self.model = model
        self.path = path

    def save(self):
        import joblib
        joblib.dump(self.model, self.path)