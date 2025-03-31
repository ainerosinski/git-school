import requests
from bs4 import BeautifulSoup
import time

def fetch_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        article_content = soup.find('div', class_='article-content').get_text()
        return article_content
    else:
        print(f"Failed to get content from {url}. Status code: {response.status_code}")

def main():
    articles = [
        "https://example.com/article1.html",
        "https://example.com/article2.html",
        # ... add more URLs as needed
    ]
    
    for article_url in articles:
        print(f"Fetching article: {article_url}")
        
        content = fetch_article(article_url)
        print(content)

if __name__ == "__main__":
    main()
