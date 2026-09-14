import pandas as pd

class machine_learning_health:
    def __init__(self):
        self.model = None
        self.data = None

    def load_data(self, data_path):
        self.data = pd.read_csv(data_path)
        for i in self.data:
            for j in self.data[i]:
                if self.data[i][j] != 0 and self.data[i][j] != 1:
                    self.data[i][j] = self.data[i].mean()

    def preprocess_data(self):
        self.preprocess_data()

    def clean_dataset(self):
        for i in self.data:
             self.data[i] = self.data[i].fillna(self.data[i].mode()[0])


    def evaluate_model(self):
        pass

    def save_model(self, model_path):
        pd.to_pickle(self.model, model_path)
        pass