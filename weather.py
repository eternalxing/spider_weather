# coding=utf-8
from bs4 import BeautifulSoup
import urllib2
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

f = open("F:/1.txt", "w+")
url = 'http://lishi.tianqi.com/changchun/201612.html'
request = urllib2.Request(url)
content = urllib2.urlopen(request).read()
soup = BeautifulSoup(content, "html.parser", from_encoding="gb18030")
data = soup.find('div', class_='tqtongji2').find_all(['ul'])
for ul in data[1:]:
    data1=ul.find_all(['li'])
    for i in data1[0:3]:
        f.write(i.string)

