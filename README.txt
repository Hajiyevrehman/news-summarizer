# News Summarizer

This is a simple news summarizer script that scrapes news articles from an RSS feed, combines them, and generates a summary using the Claude API.

## Requirements

- Python 3.x
- newspaper3k
- feedparser
- anthropic

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/news-summarizer.git
   cd news-summarizer
   ```

2. Install the required Python packages:
   ```sh
   pip install newspaper3k feedparser anthropic
   ```

3. Set your Claude API key in the environment variable `ANTHROPIC_API_KEY`.

## Usage

Run the script to get a summary of the latest news articles:
```sh
python main.py
