import requests
from dotenv import load_dotenv
import os

# Take environment variables from .env
load_dotenv()

# GET /api/v2/tickets using Basic Auth
url = "https://zccahmedabbas.zendesk.com/api/v2/tickets.json"
API_EMAIL = os.getenv("API_EMAIL")
API_TOKEN = os.getenv("API_TOKEN")
response = requests.get(url, auth=(API_EMAIL, API_TOKEN))
print(response.text)