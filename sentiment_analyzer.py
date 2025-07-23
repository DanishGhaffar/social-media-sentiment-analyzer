import pandas as pd
import numpy as np
from textblob import TextBlob
import re
import json
from datetime import datetime

class SentimentAnalyzer:
    def __init__(self):
        self.sentiment_labels = {
            'positive': 1,
            'neutral': 0,
            'negative': -1
        }
    
    def clean_text(self, text):
        """Clean and preprocess text"""
        if not isinstance(text, str):
            return ""
        
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        # Remove mentions and hashtags symbols (keep the word)
        text = re.sub(r'[@#]', '', text)
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text.strip()
    
    def get_sentiment_score(self, text):
        """Get sentiment score using TextBlob"""
        cleaned_text = self.clean_text(text)
        if not cleaned_text:
            return 0, 'neutral'
        
        blob = TextBlob(cleaned_text)
        polarity = blob.sentiment.polarity
        
        # Classify sentiment
        if polarity > 0.1:
            sentiment = 'positive'
        elif polarity < -0.1:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
            
        return polarity, sentiment
    
    def analyze_tweets(self, tweets_data):
        """Analyze sentiment for tweets"""
        if not tweets_data:
            return pd.DataFrame()
        
        results = []
        for tweet in tweets_data:
            text = tweet.get('text', '')
            polarity, sentiment = self.get_sentiment_score(text)
            
            results.append({
                'id': tweet['id'],
                'text': text,
                'cleaned_text': self.clean_text(text),
                'created_at': tweet['created_at'],
                'polarity': polarity,
                'sentiment': sentiment,
                'retweet_count': tweet.get('retweet_count', 0),
                'like_count': tweet.get('like_count', 0),
                'platform': 'twitter'
            })
        
        return pd.DataFrame(results)
    
    def analyze_reddit_posts(self, posts_data):
        """Analyze sentiment for Reddit posts"""
        if not posts_data:
            return pd.DataFrame()
        
        results = []
        for post in posts_data:
            # Combine title and text for analysis
            full_text = f"{post.get('title', '')} {post.get('text', '')}"
            polarity, sentiment = self.get_sentiment_score(full_text)
            
            results.append({
                'id': post['id'],
                'title': post.get('title', ''),
                'text': post.get('text', ''),
                'full_text': full_text,
                'cleaned_text': self.clean_text(full_text),
                'created_at': post['created_utc'],
                'polarity': polarity,
                'sentiment': sentiment,
                'score': post.get('score', 0),
                'num_comments': post.get('num_comments', 0),
                'platform': 'reddit'
            })
        
        return pd.DataFrame(results)
    
    def get_sentiment_summary(self, df):
        """Generate sentiment summary statistics"""
        if df.empty:
            return {}
        
        summary = {
            'total_posts': len(df),
            'positive_count': len(df[df['sentiment'] == 'positive']),
            'neutral_count': len(df[df['sentiment'] == 'neutral']),
            'negative_count': len(df[df['sentiment'] == 'negative']),
            'average_polarity': df['polarity'].mean(),
            'sentiment_distribution': df['sentiment'].value_counts().to_dict()
        }
        
        # Calculate percentages
        summary['positive_percentage'] = (summary['positive_count'] / summary['total_posts']) * 100
        summary['neutral_percentage'] = (summary['neutral_count'] / summary['total_posts']) * 100
        summary['negative_percentage'] = (summary['negative_count'] / summary['total_posts']) * 100
        
        return summary