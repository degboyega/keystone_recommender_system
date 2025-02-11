# 🔹 Banking Recommender System 🚀🏦  

## 📖 Overview  
This project is an **AI-powered banking product recommendation system** that helps banks suggest the **next best product** for customers based on their transaction history. It combines:  
- **Sequential Recommendation Models** (Predict next best product)  
- **LLMs (GPT-4)** (Generate personalized banking messages)  
- **Streamlit UI** (Interactive dashboard for multi-user recommendations)  
- **Azure Services** (For data storage, automation, and email alerts)  
- **Power BI** (For insights tracking)  

---

##  **Project Structure**
banking_recommender/ 
* │── main.py # Runs the Streamlit app 
*    │── recommender/ 
            │── data_loader.py # Loads and processes customer data 
            │── model.py # Defines the Sequential Recommender Model
            │── llm_generator.py # Generates personalized messages using LLM
            │── ui.py # Streamlit UI for multiple users │
            │── automation.py # Handles email/SMS automation 
            │── config.yaml # Configurations (API keys, database settings, etc.) 
            │── requirements.txt # Python dependencies 
            │── environment.yml # Conda environment file 
            │── README.md # Documentation

