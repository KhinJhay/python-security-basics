import os
import requests
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Access the variables using os.getenv
API_KEY = os.getenv("SECRET_API_KEY")
DATABASE_URL = os.getenv("DATABASE_CONNECTION_URL")

def fetch_data():
    if not API_KEY:
        print("Error: No API Key found. Check your .env file.")
        return None
        
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    # We use a try-except block here like a pro to catch connection errors
    try:
        print(f"Attempting to connect to database at: {DATABASE_URL[:15]}...")
        # response = requests.get("https://api.example.com/data", headers=headers)
        # return response.json()
        print("Success! Data fetched securely without exposing keys.")
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    print("--- Secure App Started ---")
    fetch_data()
