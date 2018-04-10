import requests, sys, webbrowser
from bs4 import BeautifulSoup
from requests.utils import urlparse


res = requests.get("http://google.com/search?q=" + "東京工科大".join(sys.argv[1:]))
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
link = soup.find_all("a")


num = min(5, len(link))
for i in range(num):
    url = link[i].get("href")
    host = urlparse(url).hostname
    urldata = requests.get(url)
    print("save:" +link[i].get("href"))
    open(host+".txt","wb").write(urldata.content)
