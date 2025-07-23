import tweepy
import praw
import json
import pandas as pd
from datetime import datetime
import config

class DataCollector:
    def __init__(self):
        self.setup_twitter_api()
        self.setup_reddit_api()
    
    def setup_twitter_api(self):
        """Initialize Twitter API client"""
        try:
            self.twitter_client = tweepy.Client(bearer_token=config.TWITTER_BEARER_TOKEN)
            print("Twitter API initialized successfully")
        except Exception as e:
            print(f"Twitter API initialization failed: {e}")
            self.twitter_client = None
    
    def setup_reddit_api(self):
        """Initialize Reddit API client"""
        try:
            self.reddit = praw.Reddit(
                client_id=config.REDDIT_CLIENT_ID,
                client_secret=config.REDDIT_CLIENT_SECRET,
                user_agent=config.REDDIT_USER_AGENT
            )
            print("Reddit API initialized successfully")
        except Exception as e:
            print(f"Reddit API initialization failed: {e}")
            self.reddit = None
    
    def collect_tweets(self, query, max_results=100):
        """Collect tweets based on search query"""
        if not self.twitter_client:
            print("Twitter API not available")
            return []
        
        tweets_data = []
        try:
            tweets = tweepy.Paginator(
                self.twitter_client.search_recent_tweets,
                query=query,
                tweet_fields=['created_at', 'author_id', 'public_metrics'],
                max_results=min(max_results, 100)
            ).flatten(limit=max_results)
            
            for tweet in tweets:
                tweets_data.append({
                    'id': tweet.id,
                    'text': tweet.text,
                    'created_at': tweet.created_at,
                    'author_id': tweet.author_id,
                    'retweet_count': tweet.public_metrics['retweet_count'],
                    'like_count': tweet.public_metrics['like_count']
                })
                
        except Exception as e:
            print(f"Error collecting tweets: {e}")
        
        return tweets_data
    
    def collect_reddit_posts(self, subreddit_name, query, limit=100):
        """Collect Reddit posts from specific subreddit"""
        if not self.reddit:
            print("Reddit API not available")
            return []
        
        posts_data = []
        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            
            # Search for posts
            for post in subreddit.search(query, limit=limit):
                posts_data.append({
                    'id': post.id,
                    'title': post.title,
                    'text': post.selftext,
                    'score': post.score,
                    'num_comments': post.num_comments,
                    'created_utc': datetime.fromtimestamp(post.created_utc),
                    'url': post.url
                })
                
        except Exception as e:
            print(f"Error collecting Reddit posts: {e}")
        
        return posts_data
    
    def save_data(self, data, filename):
        """Save collected data to JSON file"""
        with open(f'data/{filename}', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, default=str)
        print(f"Data saved to data/{filename}")