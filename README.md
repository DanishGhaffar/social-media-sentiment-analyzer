# 🎭 Social Media Sentiment Analyzer
A comprehensive Python application that analyzes sentiment from Twitter and Reddit posts, providing insights into public opinion on any topic through interactive visualizations and detailed reports.

## 🌟 Features

- **Multi-Platform Data Collection**: Fetch data from both Twitter and Reddit APIs
- **Advanced Sentiment Analysis**: Uses TextBlob for accurate sentiment classification
- **Rich Visualizations**: 
  - Sentiment distribution pie charts
  - Time series trend analysis
  - Word clouds for popular terms
  - Interactive dashboards with Plotly
- **Data Export**: Results saved in CSV and JSON formats
- **Clean Architecture**: Modular design with separate classes for different functionalities

## 📊 Sample Output

### Sentiment Distribution
![Sentiment Analysis](https://via.placeholder.com/600x400/2ecc71/ffffff?text=Sentiment+Distribution+Chart)

### Word Cloud Example
![Word Cloud](https://via.placeholder.com/600x300/3498db/ffffff?text=Word+Cloud+Visualization)

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Twitter Developer Account (optional)
- Reddit Developer Account

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/social-media-sentiment-analyzer.git
cd social-media-sentiment-analyzer
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
Create a `.env` file in the root directory:
```env
TWITTER_BEARER_TOKEN=your_twitter_bearer_token_here
REDDIT_CLIENT_ID=your_reddit_client_id_here
REDDIT_CLIENT_SECRET=your_reddit_client_secret_here
REDDIT_USER_AGENT=SentimentAnalyzer/1.0
```

4. **Run the application**
```bash
python main.py
```

## 🔧 Configuration

### Getting API Keys

#### Twitter API Setup
1. Visit [Twitter Developer Portal](https://developer.twitter.com/)
2. Apply for a developer account
3. Create a new app
4. Copy the Bearer Token to your `.env` file

#### Reddit API Setup
1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
2. Click "Create App" or "Create Another App"
3. Choose "script" for personal use
4. Copy Client ID and Client Secret to your `.env` file

### Configuration Options

Modify `config.py` to adjust:
- Maximum number of posts to collect
- Sentiment analysis thresholds
- Output file locations

```python
MAX_TWEETS = 100
MAX_REDDIT_POSTS = 100
SENTIMENT_THRESHOLD = 0.1
```

## 📖 Usage Examples

### Basic Usage
```bash
python main.py
# Enter search topic: "artificial intelligence"
# Choose platform: both
# Enter subreddit: technology
```

### Analyzing Specific Topics
- **Technology trends**: "machine learning", "blockchain", "web3"
- **Social issues**: "climate change", "healthcare", "education"
- **Entertainment**: "marvel movies", "netflix shows", "gaming"
- **Current events**: Any trending topic or news event

## 📁 Project Structure

```
sentiment_analyzer/
├── main.py                 # Main application entry point
├── data_collector.py       # API data collection logic
├── sentiment_analyzer.py   # Sentiment analysis processing
├── visualizer.py          # Chart and graph generation
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── data/                  # Raw data storage
│   ├── tweets.json
│   └── reddit_posts.json
├── output/                # Generated visualizations and reports
│   ├── sentiment_pie.png
│   ├── sentiment_bar.png
│   ├── wordcloud.png
│   ├── time_series.png
│   ├── dashboard.html
│   └── sentiment_results.csv
└── README.md
```

## 🎨 Visualization Types

### 1. Sentiment Distribution Pie Chart
Shows the percentage breakdown of positive, neutral, and negative sentiments.

### 2. Sentiment Bar Chart
Displays the count of posts for each sentiment category.

### 3. Word Cloud
Visual representation of the most frequently used words in the dataset.

### 4. Time Series Analysis
Tracks sentiment trends over time to identify patterns.

### 5. Interactive Dashboard
Plotly-powered interactive charts for deeper data exploration.

## 📊 Sample Analysis Results

```
=== SENTIMENT ANALYSIS RESULTS ===
Total posts analyzed: 150
Positive: 65 (43.3%)
Neutral: 45 (30.0%)
Negative: 40 (26.7%)
Average sentiment score: 0.125
```

## 🔍 Technical Details

### Sentiment Classification
- **Positive**: Polarity > 0.1
- **Neutral**: -0.1 ≤ Polarity ≤ 0.1  
- **Negative**: Polarity < -0.1

### Text Preprocessing
- URL removal
- Mention and hashtag cleaning
- Whitespace normalization
- Special character handling

### Libraries Used
- **Data Collection**: `tweepy`, `praw`
- **Text Analysis**: `textblob`, `pandas`
- **Visualization**: `matplotlib`, `seaborn`, `plotly`, `wordcloud`
- **Configuration**: `python-dotenv`

## 🚧 Future Enhancements

- [ ] **Advanced NLP Models**: Integration with VADER sentiment analyzer and transformers
- [ ] **Real-time Streaming**: Live sentiment tracking for trending topics
- [ ] **Web Interface**: Flask/Django web application
- [ ] **Database Integration**: PostgreSQL/MongoDB for data persistence
- [ ] **Emotion Detection**: Beyond sentiment (joy, anger, fear, etc.)
- [ ] **Comparative Analysis**: Multiple topic comparison
- [ ] **Export Options**: PDF reports and PowerPoint presentations
- [ ] **Machine Learning**: Custom sentiment models training
- [ ] **Social Network Analysis**: User influence and engagement metrics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [TextBlob](https://textblob.readthedocs.io/) for sentiment analysis
- [Tweepy](https://www.tweepy.org/) for Twitter API integration
- [PRAW](https://praw.readthedocs.io/) for Reddit API integration
- [Plotly](https://plotly.com/python/) for interactive visualizations

## 📞 Contact

**Your Name** - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/yourusername/social-media-sentiment-analyzer](https://github.com/yourusername/social-media-sentiment-analyzer)

---

⭐ **If you found this project helpful, please give it a star!** ⭐