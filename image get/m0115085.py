import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

URLFILE = 'urls.txt'
urllist = open(URLFILE).readlines()


for url in urllist:
    pagedata = requests.get(url)
    soup = BeautifulSoup(pagedata.text,'lxml')


imgs =soup.find_all('img')
for img in imgs:
    imgurl =img.get('src')
    print('URL:' ,imgurl)
    imgfullpath = urlparse(imgurl).path
    imgpath = imgfullpath.rsplit('/' , 1)[0]
    imgfname = imgfullpath.rsplit('/' , 1)[1].split('?')[0]

    if imgfname !='':
       if imgurl.endswith('jpg') or imgurl.endswith('gif') or imgurl.endswith('png'):
          imgdata = requests.get(imgurl)
          open(imgfname,'wb').write(imgdata.content)
          print('Save',imgfname)
