import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Print the loaded API key to verify
api_key = os.getenv('OMDB_API_KEY')
print(f"Loaded API Key: {api_key}")
