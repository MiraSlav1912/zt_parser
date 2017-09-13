__author__ = 'Myroslav'

from lxml.html import fromstring
import htmlmov
from datetime import date, datetime, timedelta, time
from urllib.request import urlparse
import xlwt
import sqlite3

class www_korosten:

    def get_name(self):
        return 'Новини Коростеня'

    def get_country(self):
        return 'ua'

    def get_domain(self, url):
        domain = urlparse(url)[1]
        if domain is None: return None
        domain = domain.replace('.', '_').replace('-', '_')
        return domain

    def check_on_duplicate(self, dT):
        name_db = 'All_Pars_BD.db3'
        con = sqlite3.connect(name_db)
        cur = con.cursor()
        dd = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='main'").fetchone()
        if not dd:
            return ''
        cur.execute(
            "SELECT link FROM main "
            "WHERE ({0}) and date between {1} AND {2} ".format("domain = '{0}'".format(www_korosten.get_name(0)),
                                                               int(dT) * 10000, int(dT) * 10000 + 9999))
        check_list = cur.fetchall()
        con.close()
        return check_list
    def run(self,dT):
        chek_list = www_korosten.check_on_duplicate(0, dT)
        dT = dT[-2:]+"."+ dT[4:6]+"."+dT[:4]
        i = 1
        hrf = []
        url = 'http://www.korosten.in.ua/news/page{0}/'
        #парсинг перших 4-ох сторінок
        while i < 4:
            try:
                url_ = url.format(str(i))
                page = htmlmov.url_line(url_)
                if not page: continue
                doc = fromstring(page)
                doc.make_links_absolute(url_)

                date = doc.xpath("//div[@class='news_date']")
                link_pg = doc.xpath("//div[@class='news_detalies']/a")
                hrf +=[link_pg[x].get("href") for x in range(date.__len__()) if date[x].text == dT]
                i +=1
            except Exception as ex:
                print(ex)
            continue

        [hrf.remove(j) for i in chek_list for j in hrf if i[0] == j]
        inf = [[],[],[],[],[]]
        for x in hrf:
            try:
                url_1 = x
                i = 0
                page1 = htmlmov.url_line(url_1)
                doc1 = fromstring(page1)
                doc1.make_links_absolute(url_1)

                inf[0].append(url_1)
                time = doc1.xpath("//div[@class='date']//text()")
                time = time[i][-4:] + time[i][3:5] + time[i][:2] + '1800'
                inf[1].append(time)
                inf[2].extend(doc1.xpath("//div[@class='fon_odrizat']//text()"))
                kok = []
                kok.extend(doc1.xpath("//div[@class='subBody']//p//text()"))
                inf[3].append(','.join(kok))
                kok.clear()
                inf[4].append(www_korosten.get_name(0))
            except Exception as ex:
                print(ex)
            continue
        return inf

if __name__ == '__main__':
    #корегувати дату вводу
    date_load = date.today()
    dT = str(date_load.strftime('%Y%m%d'))
    '20090101'
    dT = '20170526'
    m = www_korosten.run(0,dT)
    pass

