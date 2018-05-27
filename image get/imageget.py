import requests, sys, webbrowser
from bs4 import BeautifulSoup
from requests.utils import urlparse

word = '桜'
url = 'https://search.yahoo.co.jp/image/search?p=' + word
print('KW : ' + word)

pagedata = requests.get(url)
soup = BeautifulSoup(pagedata.text,'lxml')
imgs =soup.find_all('img')
a = 1


num = min(5, len(imgs))
for i in range(num):
    imgurl = imgs[i].get("src")
    print('URL:' ,imgurl)
    imgdata = requests.get(imgurl)
    open(word+str(a)+ ".jpg",'wb').write(imgdata.content)
    print('Save')
    a += 1
