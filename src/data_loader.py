import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        """Load customer transaction data from CSV or Database."""
        data = pd.read_csv(self.file_path)
        return data

    def preprocess(self, data):
        """Preprocess the data for recommendation."""
        data['Transaction Date'] = pd.to_datetime(data['Transaction Date'])
        data = data.sort_values(by=['Customer ID', 'Transaction Date'])
        return data
