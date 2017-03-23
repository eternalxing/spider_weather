# coding=utf-8
from bs4 import BeautifulSoup
import urllib2
import sys
import time

reload(sys)
sys.setdefaultencoding("utf-8")

month_list=['01','02','03','04','05','06','07','08','09','10','11','12']
f = open("F:/1.txt", "w+")
for year in range(2011,2016):
    for month in month_list:
        str1=str(year)+month
        url = 'http://lishi.tianqi.com/changchun/'+str1+'.html'
        request = urllib2.Request(url)
        content = urllib2.urlopen(request).read()
        soup = BeautifulSoup(content, "html.parser", from_encoding="gb18030")
        data = soup.find('div', class_='tqtongji2').find_all(['ul'])
        for ul in data[1:]:
            data1=ul.find_all(['li'])
            for i in data1[0:3]:
                f.write(i.string+" ")
            f.write('\n')
    time.sleep(1)
f.close()

