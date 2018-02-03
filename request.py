import requests
from bs4 import BeautifulSoup
url = "https://news.yahoo.co.jp/topics"
res = requests.get(url)
with open('html.text', 'w') as file:
    file.write(res.text)

bs = BeautifulSoup(res.text, "lxml")
topics = bs.select('.fl, .fr')
news_topics = {}
for news in topics:
    topic = news.select('li')[0].text
    news_topics[topic] = [news_topic.text for news_topic in news.select('li')[1:-2]]

with open('fin.text', 'w') as fin:
    fin.write(str(news_topics))
