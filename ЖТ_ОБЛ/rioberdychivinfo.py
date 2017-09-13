__author__ = 'Myroslav'

from lxml.html import fromstring
import htmlmov
from datetime import date
from urllib.request import urlparse
import xlwt
import sqlite3
class rio_berdichev:
    def get_name(self):
        return 'РІО Бердичів'

    def get_country(self):
        return 'ua'

    def get_domain(self, url):
        domain = urlparse(url)[1]
        if domain is None: return None
        domain = domain.replace('.', '_').replace('-', '_')
        return domain

    def check_on_duplicate(self, dT):
        dT = str(dT).replace("/",'')
        name_db = 'All_Pars_BD.db3'
        con = sqlite3.connect(name_db)
        cur = con.cursor()
        dd = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='main'").fetchone()
        if not dd:
            return ''
        cur.execute(
            "SELECT link FROM main "
            "WHERE ({0}) and date between {1} AND {2} ".format("domain = '{0}'".format(rio_berdichev.get_name(0)),
                                                               int(dT) * 10000, int(dT) * 10000 + 9999))
        check_list = cur.fetchall()
        con.close()
        return check_list
    def run(self,dT):
        hrf = []
        dat = []
        url = 'https://rio-berdychiv.info/component/k2/itemlist/date/{0}.html'
        try:
            #Завантажуємо код сторінки
            url_ = url.format(dT)
            page = htmlmov.url_line(url_)

            doc = fromstring(page)
            doc.make_links_absolute(url_)
            #Заванажуємо посилання повідовлень за завначену дату
            ref_news = doc.xpath("//h2/a")
            hrf += [ref_news[x].get("href") for x in range(ref_news.__len__())]

            chek_list = rio_berdichev.check_on_duplicate(0, dT)
            [hrf.remove(j) for i in chek_list for j in hrf if i[0] == j]
            d = doc.xpath("//div[@class = 'genericItemHeader']/span/text()")
            dat +=[d[x][-9:-4].replace(":",'') for x in range(len(d))]

        except Exception as ex:
                print(ex)
        inf = [[],[],[],[],[]]
        i = 0
        for x in hrf:

            try:
                url_1 = x
                page1 = htmlmov.url_line(url_1)
                doc1 = fromstring(page1)
                doc1.make_links_absolute(url_1)
                #Заповлення масиву даними
                inf[0].append(url_1)
                k = "{0}{1}".format(dT.replace("/","").replace("-",""),dat[i])
                inf[1].append(k)
                m = doc1.xpath("//h2/text()")
                m = ' '.join([x.strip() for x in m if x.strip()])
                inf[2].append(m)
                t = doc1.xpath("//div[1]/div[3]/p/text()")
                t += doc1.xpath("//div[@class = 'itemFullText']/p/text()")

                txt = ' '.join([x.strip() for x in t if x.strip()])
                if txt =='':
                    t = doc1.xpath("//div[1]/div[3]/p/strong/span/text()")
                    txt = ' '.join([x.strip() for x in t if x.strip()])
                inf[3].append(txt)
                inf[4].append(rio_berdichev.get_name(0))
            except Exception as ex:
                print(ex)
            continue
        i+=1
        return inf
if __name__ == '__main__':
        date_load = date.today()
        dT = str(date_load.strftime('%Y/%m/%d'))
        m = rio_berdichev.run(0,dT)
        pass
        #
        # wb = xlwt.Workbook()
        # ws = wb.add_sheet(rio_berdichev.get_name(0))
        # for y in range(4):
        #     for x in range(len(m[y])):
        #         ws.write(x, y, str(m[y][x]))
        # wb.save('{0}_rio_berdichev.xls'.format(dT.replace("/","-")))
