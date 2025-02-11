import openai
import yaml

class LLMMessageGenerator:
    def __init__(self, config_file="config.yaml"):
        with open(config_file, "r") as file:
            self.config = yaml.safe_load(file)
        openai.api_key = self.config["openai_api_key"]

    def generate_message(self, customer_name, product_name):
        """Generate a personalized message for the customer."""
        prompt = f"Create a short, friendly banking message for {customer_name}, recommending {product_name}."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
