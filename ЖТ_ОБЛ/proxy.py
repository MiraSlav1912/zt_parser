import requests
import lxml.html as html
import htmlmov
from datetime import date,timedelta
from urllib.request import urlparse
import sqlite3


def main():

    url = "http://chernyakhiv.org.ua/category/novyny-radomyshlya/"
    page = html.parse("%//div[@class = 'Post']//span[@class = 'PostHeader']/a" % (url))
    # #print(get_html(url))
    # page = requests.get(url)
    # tree = etree.XML(page)
    # doc = tree.xpath("")
    print(doc)

if __name__ == '__main__':
    main()
