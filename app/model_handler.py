import pickle
import numpy as np


class ModelHandler:
    def __init__(self, model_path: str):
        self.model = None
        self.load_model(model_path)

    def load_model(self, model_path):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def preprocess(self, data):
        features = np.array(list(data.values())).reshape(1, -1)
        return features

    def predict(self, data):
        features = self.preprocess(data)
        prediction = self.model.predict(features)[0]
        probability = self.model.predict_proba(features)[0][1]

        return {
            'prediction': int(prediction),
            'probability': float(probability)
        }
