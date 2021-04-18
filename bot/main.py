import os
from pathlib import Path
from dotenv import load_dotenv

from user import User

path = Path('config/.env')
load_dotenv(dotenv_path=path)

API_URL = os.getenv('API_URL')
MAX_USERS = int(os.getenv('BOT_USERS_COUNT'))
MAX_POSTS = int(os.getenv('BOT_MAX_POSTS'))
MAX_LIKES = int(os.getenv('BOT_MAX_LIKES'))

# TODO change functionality and make async
for i in range(MAX_USERS):
    user = User(API_URL)
    for j in range(MAX_POSTS):
        user.create_post()
    for k in range(MAX_LIKES):
        user.like_post()
