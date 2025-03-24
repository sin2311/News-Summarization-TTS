# -*- coding: utf-8 -*-
"""utils/news_scraper.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17kQKbboQ9nsspKl8GgPaOOrP3B9nKoFW
"""

import nltk
nltk.download('punkt')



import requests
from bs4 import BeautifulSoup
from newspaper import Article
import nltk
import time
import urllib.parse
from typing import List, Dict
from tenacity import retry, stop_after_attempt, wait_exponential

# Download required NLTK resources
def download_nltk_resources():
    nltk.download("punkt", quiet=True)
    nltk.download("averaged_perceptron_tagger", quiet=True)

download_nltk_resources()

def clean_url(url: str) -> str:
    """Decode URL properly"""
    return urllib.parse.unquote(url)

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=1, max=5))
def fetch_news_rss(company_name: str) -> List[Dict[str, str]]:
    """Fetch top 10 news articles from Bing News RSS."""
    search_url = f"https://www.bing.com/news/search?q={urllib.parse.quote(company_name)}&format=rss"
    response = requests.get(search_url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "xml")
    return soup.find_all("item")[:10]

def process_article(url: str, fallback_title: str, fallback_summary: str) -> Dict[str, str]:
    """Extract content from the article URL with NLP fallback"""
    try:
        article = Article(url, timeout=20)
        article.download()
        time.sleep(1)  # Prevent overloading servers
        article.parse()
        article.nlp()

        return {
            "title": article.title or fallback_title,
            "url": url,
            "summary": article.summary or fallback_summary,
            "content": article.text[:500],  # Limit content length
            "publish_date": str(article.publish_date) if article.publish_date else None,
            "authors": article.authors if article.authors else [],
        }
    except Exception as e:
        print(f"⚠️ Error processing article: {e}")
        return {
            "title": fallback_title,
            "url": url,
            "summary": fallback_summary,
            "content": fallback_summary,
            "publish_date": None,
            "authors": [],
        }

def get_news_articles(company_name: str) -> List[Dict[str, str]]:
    """Main function to fetch and process news articles."""
    print(f"\n🔍 Searching for news about: {company_name}")
    try:
        items = fetch_news_rss(company_name)
        print(f"✅ Found {len(items)} news articles.")

        articles = []
        for item in items:
            rss_title = item.title.text if item.title else ""
            rss_summary = item.description.text if item.description else ""
            url = clean_url(item.link.text if item.link else "")

            print(f"📄 Processing: {rss_title}")
            article_data = process_article(url, rss_title, rss_summary)
            articles.append(article_data)

        return articles

    except requests.RequestException as e:
        print(f"❌ Error fetching news: {e}")
        return []

if __name__ == "__main__":
    company = "Microsoft"
    articles = get_news_articles(company)

    # Print formatted output
    print(f"\n📰 **Top {len(articles)} News Articles**\n")
    for i, article in enumerate(articles, 1):
        print(f"### {i}. {article['title']}")
        print(f"📌 **URL:** [Read here]({article['url']})")
        print(f"📖 **Summary:** {article['summary'][:250]}...")
        if article["authors"]:
            print(f"✍️ **Authors:** {', '.join(article['authors'])}")
        print("-" * 80)