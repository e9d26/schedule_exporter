import requests
url = "https://news.yahoo.co.jp/topics"
res = requests.get(url)
with open('html.text', 'w') as file:
    file.write(res.text)
