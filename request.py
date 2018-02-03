import requests
url = "https://news.yahoo.co.jp/topics"
res = requests.get(url)
res.status_code
