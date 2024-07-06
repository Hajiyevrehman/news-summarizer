import os
import newspaper
import feedparser
import anthropic

# Set your API key here or use environment variable
API_KEY = os.getenv('ANTHROPIC_API_KEY')

# Initialize the Anthropic client with your API key
client = anthropic.Anthropic(api_key=API_KEY)

def summarize_text_with_claude(text):
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        system="You are a summarization AI. Summarize the following news article content.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": text
                    }
                ]
            }
        ]
    )
    summarized_text = "".join(block.text for block in message.content)
    return summarized_text

def scrape_news_from_feed(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        article = newspaper.Article(entry.link)
        article.download()
        article.parse()
        articles.append(article.text)
    return articles

feed_url = 'http://feeds.bbci.co.uk/news/rss.xml'
articles = scrape_news_from_feed(feed_url)

# Combine all articles into one string
all_articles_content = "\n\n".join(articles)

# Summarize the combined content
summary = summarize_text_with_claude(all_articles_content)

# Print the summary
print("Summary of all articles:")
print(summary)
