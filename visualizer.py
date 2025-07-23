import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class SentimentVisualizer:
    def __init__(self):
        plt.style.use('seaborn-v0_8')
        self.colors = {
            'positive': '#2ecc71',
            'neutral': '#95a5a6',
            'negative': '#e74c3c'
        }
    
    def create_sentiment_pie_chart(self, summary, save_path='output/sentiment_pie.png'):
        """Create pie chart of sentiment distribution"""
        labels = ['Positive', 'Neutral', 'Negative']
        sizes = [
            summary['positive_percentage'],
            summary['neutral_percentage'],
            summary['negative_percentage']
        ]
        colors = [self.colors['positive'], self.colors['neutral'], self.colors['negative']]
        
        plt.figure(figsize=(10, 8))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.title('Sentiment Distribution', fontsize=16, fontweight='bold')
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        print(f"Pie chart saved to {save_path}")
    
    def create_sentiment_bar_chart(self, df, save_path='output/sentiment_bar.png'):
        """Create bar chart of sentiment counts"""
        sentiment_counts = df['sentiment'].value_counts()
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(sentiment_counts.index, sentiment_counts.values, 
                      color=[self.colors[sent] for sent in sentiment_counts.index])
        
        plt.title('Sentiment Analysis Results', fontsize=16, fontweight='bold')
        plt.xlabel('Sentiment', fontsize=12)
        plt.ylabel('Number of Posts', fontsize=12)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                    f'{int(height)}', ha='center', va='bottom', fontsize=11)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        print(f"Bar chart saved to {save_path}")
    
    def create_wordcloud(self, df, sentiment='all', save_path='output/wordcloud.png'):
        """Create word cloud from text data"""
        if sentiment != 'all':
            text_data = df[df['sentiment'] == sentiment]['cleaned_text'].str.cat(sep=' ')
            title = f'Word Cloud - {sentiment.capitalize()} Sentiment'
        else:
            text_data = df['cleaned_text'].str.cat(sep=' ')
            title = 'Word Cloud - All Sentiments'
        
        if not text_data.strip():
            print("No text data available for word cloud")
            return
        
        wordcloud = WordCloud(
            width=800, 
            height=400, 
            background_color='white',
            colormap='viridis',
            max_words=100
        ).generate(text_data)
        
        plt.figure(figsize=(12, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        print(f"Word cloud saved to {save_path}")
    
    def create_time_series_plot(self, df, save_path='output/time_series.png'):
        """Create time series plot of sentiment over time"""
        if df.empty or 'created_at' not in df.columns:
            print("No time data available")
            return
        
        df['created_at'] = pd.to_datetime(df['created_at'])
        df['date'] = df['created_at'].dt.date
        
        # Group by date and sentiment
        daily_sentiment = df.groupby(['date', 'sentiment']).size().reset_index(name='count')
        daily_sentiment_pivot = daily_sentiment.pivot(index='date', columns='sentiment', values='count').fillna(0)
        
        plt.figure(figsize=(12, 6))
        for sentiment in daily_sentiment_pivot.columns:
            plt.plot(daily_sentiment_pivot.index, daily_sentiment_pivot[sentiment], 
                    marker='o', label=sentiment.capitalize(), color=self.colors[sentiment])
        
        plt.title('Sentiment Trends Over Time', fontsize=16, fontweight='bold')
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Number of Posts', fontsize=12)
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        print(f"Time series plot saved to {save_path}")
    
    def create_interactive_dashboard(self, df, summary):
        """Create interactive dashboard using Plotly"""
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Sentiment Distribution', 'Polarity Distribution', 
                          'Platform Comparison', 'Top Words'),
            specs=[[{"type": "pie"}, {"type": "histogram"}],
                   [{"type": "bar"}, {"type": "bar"}]]
        )
        
        # Pie chart
        fig.add_trace(
            go.Pie(labels=['Positive', 'Neutral', 'Negative'],
                   values=[summary['positive_count'], summary['neutral_count'], summary['negative_count']],
                   marker_colors=[self.colors['positive'], self.colors['neutral'], self.colors['negative']]),
            row=1, col=1
        )
        
        # Polarity histogram
        fig.add_trace(
            go.Histogram(x=df['polarity'], nbinsx=30, name='Polarity'),
            row=1, col=2
        )
        
        # Platform comparison
        if 'platform' in df.columns:
            platform_sentiment = df.groupby(['platform', 'sentiment']).size().reset_index(name='count')
            for sentiment in ['positive', 'neutral', 'negative']:
                data = platform_sentiment[platform_sentiment['sentiment'] == sentiment]
                fig.add_trace(
                    go.Bar(x=data['platform'], y=data['count'], name=sentiment.capitalize(),
                           marker_color=self.colors[sentiment]),
                    row=2, col=1
                )
        
        fig.update_layout(height=800, showlegend=True, title_text="Sentiment Analysis Dashboard")
        fig.show()
        
        # Save as HTML
        fig.write_html("output/dashboard.html")
        print("Interactive dashboard saved to output/dashboard.html")