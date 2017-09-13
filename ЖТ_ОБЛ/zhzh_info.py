__author__ = 'Myroslav'

from lxml.html import fromstring
import htmlmov
from datetime import date,timedelta
from urllib.request import urlparse
import sqlite3

class zhzh_info:
    def get_name(self):
        return 'Журнал Житомира'

    def get_country(self):
        return 'ua'

    def get_domain(self, url):
        domain = urlparse(url)[1]
        if domain is None: return None
        domain = domain.replace('.', '_').replace('-', '_')
        return domain
    def check_on_duplicate(self,dT):
        name_db = 'All_Pars_BD.db3'
        con = sqlite3.connect(name_db)
        cur = con.cursor()
        dd = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='main'").fetchone()
        if not dd:
            return ''
        dT  = str(dT).replace("-",'')
        cur.execute(
            "SELECT link FROM main "
            "WHERE ({0}) and date between {1} AND {2} ".format("domain = '{0}'".format(zhzh_info.get_name(0)), int(dT) * 10000, int(dT) * 10000 + 9999))
        check_list = cur.fetchall()
        con.close()
        return check_list
    def run(self, dT):
        hrf = []
        url = 'http://zhzh.info/news/{0}'#2017-02-09
        chek_list = zhzh_info.check_on_duplicate(0, dT)
        try:
            #Завантажуємо код сторінки
            url_ = url.format(dT)
            page = htmlmov.url_line(url_)
            doc = fromstring(page)
            doc.make_links_absolute(url_)
            #Заванажуємо посилання повідовлень за зазначену дату
            ref_news = doc.xpath("//div[@class = 'entry-title']/a")
            hrf += [ref_news[x].get("href") for x in range(ref_news.__len__())]
            [hrf.remove(j) for i in chek_list for j in hrf if i[0] == j]
        except Exception as ex:
                print(ex)
        inf = [[],[],[],[],[]]

        for x in hrf:
            try:
                url_1 = x
                page1 = htmlmov.url_line(url_1)
                doc1 = fromstring(page1)
                doc1.make_links_absolute(url_1)
                #Заповлення масиву даними
                inf[0].append(url_1)

                date_load = date.today()
                Today = str(date_load.strftime('%Y-%m-%d'))
                Yest = date.today() - timedelta(1)
                Yesterday = Yest.strftime('%Y-%m-%d')
                st = -8
                ed = -4
                if dT == Today:
                    st = 11
                    ed = -4
                if dT == Yesterday:
                    st = 9
                    ed = -4
                k = '{0}{1}'.format(dT.replace("-",""),str(doc1.xpath("//div[@class = 'full-entry-details entry-details']/span[1]/text()")).replace(":","")[st:ed])
                #k = str(doc1.xpath("//div[@class = 'full-entry-details entry-details']/span[1]/text()"))
                inf[1].append(k)
                inf[2].extend(doc1.xpath("//h1/text()"))
                t = doc1.xpath("//div[@class = 'full-entry-text entry-text']//p/text()")
                t += doc1.xpath("//div[@class = 'full-entry-text entry-text']/text()")
                txt = ' '.join([x.strip() for x in t if x.strip()])
                inf[3].append(txt)
                inf[4].append(str(zhzh_info.get_name(0)))
            except Exception as ex:
                print(ex)
            continue
        return inf

if __name__ == '__main__':
        date_load = date.today()
        dT = str(date_load.strftime('%Y-%m-%d'))
        m = zhzh_info.run(0,dT)
        pass



