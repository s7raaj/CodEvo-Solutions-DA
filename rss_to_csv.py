import feedparser
from newspaper import Article
import csv

def parse_rss_feed(rss_url):
  
    feed = feedparser.parse(rss_url)
    articles_info = []

    if not feed.entries:
        print(f"No articles found in feed: {rss_url}")
        return articles_info
   
    for entry in feed.entries:
        article_url = entry.link
        
        try:
           
            article = Article(article_url)
            article.download()
            article.parse()
            
           
            title = article.title
            author = article.authors if article.authors else ["No author"]
            publish_date = article.publish_date if article.publish_date else "No publish date"
            content = article.text
            
         
            articles_info.append({
                'title': title,
                'author': ', '.join(author),  
                'publish_date': publish_date,
                'content': content
            })
        except Exception as e:
            print(f"Error processing article {article_url}: {e}")
    
    return articles_info
def save_as_csv(articles_info, filename='articles.csv'):
    keys = articles_info[0].keys()  
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(articles_info)
rss_urls = [
    'http://feeds.bbci.co.uk/news/rss.xml',
    'https://rss.cnn.com/rss/cnn_topstories.rss',
    'https://www.theverge.com/rss/index.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    'https://lifehacker.com/rss',
    'https://www.wired.com/feed/rss'
]

for url in rss_urls:
    print(f"Parsing feed: {url}")
    articles = parse_rss_feed(url)
    if articles:
        save_as_csv(articles, filename='articles.csv')
        print(f"Saved {len(articles)} articles to 'articles.csv'")
    else:
        print(f"No articles to save for feed: {url}")
