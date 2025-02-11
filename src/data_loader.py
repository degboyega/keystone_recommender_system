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
        data['transaction_date'] = pd.to_datetime(data['transaction_date'])
        data = data.sort_values(by=['customer_id', 'transaction Date'])
        return data
