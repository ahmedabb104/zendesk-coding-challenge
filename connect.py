import requests
from dotenv import load_dotenv
import os

# Take environment variables from .env
load_dotenv()

# GET /api/v2/tickets using API token and email, storing it in response variable
URL = os.getenv("URL")
API_EMAIL = os.getenv("API_EMAIL")
API_TOKEN = os.getenv("API_TOKEN")
response = requests.get(URL, auth=(API_EMAIL, API_TOKEN))