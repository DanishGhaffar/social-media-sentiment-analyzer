import os
import pandas as pd
from data_collector import DataCollector
from sentiment_analyzer import SentimentAnalyzer
from visualizer import SentimentVisualizer
import config

def main():
    # Create necessary directories
    os.makedirs('data', exist_ok=True)
    os.makedirs('output', exist_ok=True)
    
    print("=== Social Media Sentiment Analyzer ===\n")
    
    # Get user input
    query = input("Enter search topic/keyword: ")
    platform = input("Choose platform (twitter/reddit/both): ").lower()
    
    # Initialize components
    collector = DataCollector()
    analyzer = SentimentAnalyzer()
    visualizer = SentimentVisualizer()
    
    all_results = pd.DataFrame()
    
    # Collect and analyze Twitter data
    if platform in ['twitter', 'both']:
        print(f"\nCollecting tweets about '{query}'...")
        tweets = collector.collect_tweets(query, config.MAX_TWEETS)
        
        if tweets:
            collector.save_data(tweets, 'tweets.json')
            twitter_results = analyzer.analyze_tweets(tweets)
            all_results = pd.concat([all_results, twitter_results], ignore_index=True)
            print(f"Analyzed {len(twitter_results)} tweets")
        else:
            print("No tweets collected")
    
    # Collect and analyze Reddit data
    if platform in ['reddit', 'both']:
        subreddit = input("Enter subreddit name (default: all): ") or "all"
        print(f"\nCollecting Reddit posts about '{query}' from r/{subreddit}...")
        
        reddit_posts = collector.collect_reddit_posts(subreddit, query, config.MAX_REDDIT_POSTS)
        
        if reddit_posts:
            collector.save_data(reddit_posts, 'reddit_posts.json')
            reddit_results = analyzer.analyze_reddit_posts(reddit_posts)
            all_results = pd.concat([all_results, reddit_results], ignore_index=True)
            print(f"Analyzed {len(reddit_results)} Reddit posts")
        else:
            print("No Reddit posts collected")
    
    if all_results.empty:
        print("No data collected. Please check your API credentials and try again.")
        return
    
    # Generate summary
    summary = analyzer.get_sentiment_summary(all_results)
    
    # Display results
    print("\n=== SENTIMENT ANALYSIS RESULTS ===")
    print(f"Total posts analyzed: {summary['total_posts']}")
    print(f"Positive: {summary['positive_count']} ({summary['positive_percentage']:.1f}%)")
    print(f"Neutral: {summary['neutral_count']} ({summary['neutral_percentage']:.1f}%)")
    print(f"Negative: {summary['negative_count']} ({summary['negative_percentage']:.1f}%)")
    print(f"Average sentiment score: {summary['average_polarity']:.3f}")
    
    # Save results
    all_results.to_csv('output/sentiment_results.csv', index=False)
    print(f"\nDetailed results saved to output/sentiment_results.csv")
    
    # Create visualizations
    print("\nGenerating visualizations...")
    visualizer.create_sentiment_pie_chart(summary)
    visualizer.create_sentiment_bar_chart(all_results)
    visualizer.create_wordcloud(all_results)
    visualizer.create_time_series_plot(all_results)
    visualizer.create_interactive_dashboard(all_results, summary)
    
    print("\n=== Analysis Complete! ===")
    print("Check the 'output' folder for all visualizations and results.")

if __name__ == "__main__":
    main()