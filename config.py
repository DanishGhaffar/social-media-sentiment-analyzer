import os
from dotenv import load_dotenv

load_dotenv()

# Twitter API credentials
TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Reddit API credentials
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')

# Analysis settings
MAX_TWEETS = 100
MAX_REDDIT_POSTS = 100
SENTIMENT_THRESHOLD = 0.1  # Threshold for neutral sentiment