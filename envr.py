import os
from dotenv import load_dotenv

load_dotenv('C:/Users/zawis/Documents/EV/.env')

CLIENT_ID = os.getenv('MTM_client_id')
CLIENT_SECRET = os.getenv('MTM_client_secret')
URI = os.getenv('uri')