__author__ = 'Myroslav'

from lxml.html import fromstring
import htmlmov
from datetime import date,timedelta
from urllib.request import urlparse
import sqlite3

class ovruch:
    def get_name(self):
        return 'Овруч'

    def get_country(self):
        return 'ua'

    def get_domain(self, url):
        domain = urlparse(url)[1]
        if domain is None: return None
        domain = domain.replace('.', '_').replace('-', '_')
        return domain
    #Вилучення дублікату
    def check_on_duplicate(self,dT):
        name_db = 'All_Pars_BD.db3'
        con = sqlite3.connect(name_db)
        cur = con.cursor()
        dd = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='main'").fetchone()
        if not dd:
            return ''
        cur.execute(
            "SELECT link FROM main "
            "WHERE ({0}) and date between {1} AND {2} ".format("domain = '{0}'".format(ovruch.get_name(0)), int(dT) * 10000, int(dT) * 10000 + 9999))
        if str(cur.fetchall()) == '[]':
            check_list = [[0]]
        else:
            check_list = cur.fetchall()

        con.close()
        return check_list
    def run(self, dT):
        hrf = []
        url = 'http://123ru.net/ovruch/{0}/'#2017-02-09
        inf = [[], [], [], [], []]
        chek_list = ovruch.check_on_duplicate(0, dT)

        try:
            #Завантажуємо код сторінки
            dTt = dT[:4] + '-' + dT[4:6] + '-' + dT[-2:]
            url_ = url.format(dTt)
            if url_ == chek_list[0][0]:
                url_ = None
            page = htmlmov.url_line(url_)
            doc = fromstring(page)
            #doc.make_links_absolute(url_)

            d = doc.xpath("//div/time/text()")
            dat = str(d[0][-5:]).replace(":", '')

            inf[0].append(url_)
            k = '{0}{1}'.format(dT, dat)
            inf[1].append(k)
            inf[2].extend(doc.xpath('//h3/a/text()'))

            t = doc.xpath("//div[@class = 's29_body s29_favicons']//p/text()")
            txt = ','.join([x.strip() for x in t if x.strip()])

            inf[3].append(txt)
            inf[4].append(str(ovruch.get_name(0)))

        except Exception as ex:
                print(ex)
        return inf

if __name__ == '__main__':
        date_load = date.today()
        dT = str(date_load.strftime('%Y%m%d'))
        dT = '20170525'
        m = ovruch.run(0,'20170525')
        pass