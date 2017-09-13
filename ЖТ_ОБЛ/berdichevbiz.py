__author__ = 'Myroslav'

from lxml.html import fromstring
import htmlmov
from datetime import date, datetime, timedelta, time
from urllib.request import urlparse
import xlwt
import sqlite3
mn_ua = {'Січень': '01', 'Лютий': '02', 'Березень': '03', 'Квітень': '04',
         'Травень': '05', 'Червень': '06', 'Липепь': '07', 'Серпень': '08',
         'Вересень': '09', 'Жовтень': '10', 'Листопад': '11', 'Грудень': '12'}
class berdichev_biz:

    def get_name(self):
        return 'Бердичів BIZ'

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
        cur.execute(
            "SELECT link FROM main "
            "WHERE ({0}) and date between {1} AND {2} ".format("domain = '{0}'".format(berdichev_biz.get_name(0)), int(dT) * 10000, int(dT) * 10000 + 9999))
        check_list = cur.fetchall()
        con.close()
        return check_list
    def run(self,dT):

        url = 'http://www.berdichev.biz/%D0%BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8/%D0%BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8-%D0%B1%D0%B5%D1%80%D0%B4%D0%B8%D1%87%D0%B5%D0%B2%D0%B0/'#2017-02-09
        ref =[]

        try:
            t= []
            hef = []
            #Завантажуємо код сторінки
            url_ = url
            page = htmlmov.url_line(url_)
            doc = fromstring(page)
            doc.make_links_absolute(url_)
            #Заванажуємо посилання повідовлень за завначену дату з викорситанням умови
            time = doc.xpath("//span[1]/time/text()")
            time_ = [mn_ua[str(time[x]).replace(",","").replace(" ","")[:-6]] + str(time[x]).replace(",","").replace(" ","")[-6:] for x in range(time.__len__())]
            re = doc.xpath("//h2/a")
            hef += [re[x].get("href") for x in range(re.__len__())]
            dTT = '{0}{1}{2}'.format(dT[4:6],dT[-2:],dT[:4])
            ref = [hef[x] for x in range(hef.__len__()) if time_[x] == dTT ]
            chek_list = berdichev_biz.check_on_duplicate(0, dT)
            [ref.remove(j) for i in chek_list for j in ref if i[0] == j]
        except Exception as ex:
                print(ex)
        inf = [[],[],[],[],[]]
        for x in ref:
            try:
                url_1 = x
                page1 = htmlmov.url_line(url_1)
                doc1 = fromstring(page1)
                doc1.make_links_absolute(url_1)
                #Заповлення масиву даними
                inf[0].append(url_1)
                inf[1].append(dT+'1200')
                inf[2].extend(doc1.xpath("//h1/text()"))
                t = doc1.xpath("//div[@class = 'entry-content']/p/text()")

                txt = ' '.join([x.strip() for x in t if x.strip()])
                inf[3].append(txt)
                inf[4].append(berdichev_biz.get_name(0))

            except Exception as ex:
                print(ex)
            continue
        return inf

if __name__ == '__main__':
        date_load = date.today()
        dT = str(date_load.strftime('%Y%m%d'))
        m = berdichev_biz.run(0,dT)
        pass
        # wb = xlwt.Workbook()
        # ws = wb.add_sheet(berdichev_biz.get_name(0))
        # for y in range(4):
        #     for x in range(len(m[y])):
        #         ws.write(x, y, str(m[y][x]))
        # wb.save('{0}_berdichev_biz.xls'.format(str(date_load.strftime('%Y-%m-%d'))))

