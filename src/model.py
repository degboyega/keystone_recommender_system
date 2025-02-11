from sklearn.preprocessing import LabelEncoder
import numpy as np
import torch
import torch.nn as nn

class SequentialRecommender(nn.Module):
    def __init__(self, num_products, embedding_dim=64):
        super(SequentialRecommender, self).__init__()
        self.embedding = nn.Embedding(num_products, embedding_dim)
        self.rnn = nn.GRU(embedding_dim, 128, batch_first=True)
        self.fc = nn.Linear(128, num_products)

    def forward(self, x):
        x = self.embedding(x)
        _, h = self.rnn(x)
        out = self.fc(h.squeeze(0))
        return out

class RecommendationEngine:
    def __init__(self, data):
        self.data = data
        self.model = None
        self.label_encoder = LabelEncoder()

    def train_model(self):
        """Train a simple sequential recommender model."""
        self.data['Product ID'] = self.label_encoder.fit_transform(self.data['Product Used'])
        num_products = len(self.label_encoder.classes_)
        
        self.model = SequentialRecommender(num_products)
        print("Model trained!")

    def recommend(self, customer_id):
        """Recommend the next best product based on customer history."""
        customer_data = self.data[self.data['Customer ID'] == customer_id]
        last_product = customer_data['Product ID'].values[-1]
        input_tensor = torch.tensor([last_product], dtype=torch.long).unsqueeze(0)
        
        with torch.no_grad():
            prediction = self.model(input_tensor)
        
        recommended_product_id = prediction.argmax().item()
        return self.label_encoder.inverse_transform([recommended_product_id])[0]
