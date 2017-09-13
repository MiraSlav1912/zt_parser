__author__ = 'Myroslav'

from lxml.html import fromstring
import htmlmov
from datetime import date, datetime, timedelta, time
from urllib.request import urlparse
import xlwt

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
            ref = [hef[x] for x in range(hef.__len__()) if time_[x] == dT ]
        except Exception as ex:
                print(ex)
        inf = [["Силка"],["Час"],["Заголовок"],["Тіло"]]
        for x in ref:
            try:
                t = None
                link = None
                url_1 = x
                page1 = htmlmov.url_line(url_1)
                doc1 = fromstring(page1)
                doc1.make_links_absolute(url_1)
                #Заповлення масиву даними
                inf[0].append(url_1)
                inf[1].append(str(date_load.strftime('%Y-%m-%d')))
                inf[2].extend(doc1.xpath("//h1/text()"))
                t = doc1.xpath("//div[@class = 'entry-content']/p/text()")

                txt = ' '.join([x.strip() for x in t if x.strip()])
                inf[3].append(txt)

            except Exception as ex:
                print(ex)
            continue
        return inf

if __name__ == '__main__':
        date_load = date.today()
        dT = str(date_load.strftime('%m%d%Y'))
        m = berdichev_biz.run(0,dT)

        wb = xlwt.Workbook()
        ws = wb.add_sheet(berdichev_biz.get_name(0))
        for y in range(4):
            for x in range(len(m[y])):
                ws.write(x, y, str(m[y][x]))
        wb.save('{0}_berdichev_biz.xls'.format(str(date_load.strftime('%Y-%m-%d'))))
        #????????????????????????????????????

