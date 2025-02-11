import streamlit as st
import pandas as pd
from recommender.data_loader import DataLoader
from recommender.model import RecommendationEngine
from recommender.llm_generator import LLMMessageGenerator

class BankingRecommenderUI:
    def __init__(self):
        self.data_loader = DataLoader("customer_transactions.csv")
        self.data = self.data_loader.load_data()
        self.data = self.data_loader.preprocess(self.data)
        self.recommender = RecommendationEngine(self.data)
        self.recommender.train_model()
        self.llm = LLMMessageGenerator()

    def run(self):
        st.title("🔹 Banking Product Recommender System")
        
        customer_ids = st.multiselect("Select Customers", self.data["Customer ID"].unique())

        if st.button("Generate Recommendations"):
            recommendations = []
            for customer_id in customer_ids:
                recommended_product = self.recommender.recommend(customer_id)
                customer_name = f"Customer {customer_id}"  # In real case, fetch actual name
                message = self.llm.generate_message(customer_name, recommended_product)
                recommendations.append([customer_id, recommended_product, message])
            
            df = pd.DataFrame(recommendations, columns=["Customer ID", "Recommended Product", "Personalized Message"])
            st.table(df)

if __name__ == "__main__":
    app = BankingRecommenderUI()
    app.run()
