from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.nmc.cn'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'lxml')
content = soup.select('#alarmtip > ul > li.waring > a')

for n in content:
    link = n.get('href')
    title = n.get('title')
    tag = n.text
    print(tag, url + link, title)
