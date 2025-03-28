# -*- coding: utf-8 -*-
"""utils/gemini_service.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-fuebO_Mt-RRd8AQKbcislEXuGqrgAsS
"""

from transformers import pipeline
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import torch

nltk.download("vader_lexicon")

# Load NLP models with GPU support
device = 0 if torch.cuda.is_available() else -1  # Use GPU if available
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)
sia = SentimentIntensityAnalyzer()

def process_articles(company, articles):
    processed_articles = []

    for article in articles:
        try:
            content = article.get("content", "").strip()
            title = article.get("title", "No Title")
            url = article.get("url", "#")

            if not content:
                print(f"Skipping article '{title}': No content available.")
                continue

            # Limit input length (BART max: ~1024 tokens)
            content = " ".join(content.split()[:900])  # Truncate if too long

            # Generate summary
            summary = summarizer(content, max_length=50, min_length=10, do_sample=False)[0]["summary_text"]

            # Perform sentiment analysis
            sentiment_score = sia.polarity_scores(summary)
            sentiment = (
                "Positive" if sentiment_score["compound"] > 0.05 else
                "Negative" if sentiment_score["compound"] < -0.05 else "Neutral"
            )

            processed_articles.append({
                "Title": title,
                "URL": url,
                "Summary": summary,
                "Sentiment": sentiment
            })

        except Exception as e:
            print(f"Error processing article '{title}': {e}")

    return processed_articles

def process_articles(company, articles):
    processed_articles = []

    for article in articles:
        input_length = len(article["content"].split())  # Count words in the article
        max_len = min(50, max(10, input_length // 2))  # Ensure max_length is meaningful

        summary = summarizer(article["content"], max_length=max_len, min_length=5, do_sample=False)[0]["summary_text"]
        sentiment_score = sia.polarity_scores(summary)

        sentiment = "Positive" if sentiment_score["compound"] > 0.05 else "Negative" if sentiment_score["compound"] < -0.05 else "Neutral"

        processed_articles.append({
            "Title": article["title"],
            "URL": article["url"],
            "Summary": summary,
            "Sentiment": sentiment
        })

    return processed_articles

# Example input data
articles = [
    {
        "title": "Tech Company Expands Operations",
        "url": "https://example.com/news1",
        "content": "TechCorp has announced its expansion into new markets. The company is aiming to increase its customer base."
    },
    {
        "title": "Market Crash Warning",
        "url": "https://example.com/news2",
        "content": "Financial experts have warned about an upcoming market crash due to economic instability."
    }
]

# Call the function
company = "TechCorp"
result = process_articles(company, articles)

# Print output
for article in result:
    print(article)