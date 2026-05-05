import pickle
import numpy as np
import pandas as pd


class ModelHandler:
    def __init__(self, model_path: str):
        self.model = None
        self.features = None
        self.model_version = None
        self.load_model(model_path)

    def load_model(self, model_path):
        with open(model_path, 'rb') as f:
            model_package = pickle.load(f)
            # print(model_package)

        self.model = model_package['model']
        self.features = model_package['features']
        self.model_version = model_package['model_version']


    def preprocess(self, data):
        missing_features = [feature for feature in self.features if feature not in data]

        if missing_features:
            raise ValueError(f"Missing features: {missing_features}")

        df = pd.DataFrame([data])
        df = df[self.features]

        return df


    def predict(self, data):
        features = self.preprocess(data)

        prediction = self.model.predict(features)[0]
        probability = self.model.predict_proba(features)[0][1]

        return {
            'prediction': int(prediction),
            'probability': float(probability),
            'model_version': self.model_version
        }
