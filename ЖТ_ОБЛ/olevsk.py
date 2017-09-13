from lxml.html import fromstring
import htmlmov
from datetime import date
from urllib.request import urlparse
import sqlite3

class olevsk:
    def get_name(self):
        return 'Олевськ'

    def get_country(self):
        return 'ua'

    def get_domain(self, url):
        domain = urlparse(url)[1]
        if domain is None: return None
        domain = domain.replace('.', '_').replace('-', '_')
        return domain
    # Вилучення дублікату
    def check_on_duplicate(self, dT):
        name_db = 'All_Pars_BD.db3'
        con = sqlite3.connect(name_db)
        cur = con.cursor()
        dd = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='main'").fetchone()
        if not dd:
            return ''
        cur.execute(
            "SELECT link FROM main "
            "WHERE ({0}) and date between {1} AND {2} ".format("domain = '{0}'".format(olevsk().get_name()),
                                                               int(dT) * 10000, int(dT) * 10000 + 9999))
        check_list = cur.fetchall()
        con.close()
        return check_list

    def run(self,dT):
        hrf = []
        url = 'http://olevsk.com.ua/arhiv?page={0}'
        chek_list = olevsk().check_on_duplicate(dT)
        dat = []
        j = 0
        while j < 5:
            try:
                #url = 'http://olevsk.com.ua/arhiv?page={0}/'.format(j)
                # Завантажуємо код сторінки
                page = htmlmov.url_line(url)
                doc = fromstring(page)
                doc.make_links_absolute(url)
                # dat = doc.xpath(
                #     "//div[@class = 'left-corner']//table[@class = 'views-table cols-2']/caption/text()")
                # dat = [dat[x][-4:] + dat[x][3:5] + dat[x][:2] for x in range(dat.__len__())]
                ref_news = doc.xpath("//div[@class = 'left-corner']//td[@class = 'views-field views-field-title']/a")
                dat = doc.xpath(
                    "//div[@class = 'left-corner']//td[@class = 'views-field views-field-title']/text()[2]")
                dat = [dat[x][6:10]+dat[x][3:5]+dat[x][:2] for x in range(dat.__len__())]
                hrf += [ref_news[x].get("href") for x in range(ref_news.__len__()) if dT == dat[x]]
                if not hrf:
                    break
                j+=1
                pass
            except Exception as ex:
                print(ex)

        inf = [[],[],[],[],[]]
        for x in hrf:
            try:
                page1 = htmlmov.url_line(x)
                doc1 = fromstring(page1)
                doc1.make_links_absolute(x)
                #Заповлення масиву даними
                inf[0].append(x)
                page_date = doc1.xpath("//span[@class = 'submitted']/text()")
                inf[1].append(page_date[0][11:15] + page_date[0][8:10] + page_date[0][5:7] + page_date[0][-5:-3] + page_date[0][-2:])

                inf[2].append(doc1.xpath("//div[@class ='left-corner']/h2/text()"))
                t = []
                t += doc1.xpath("//div[@class ='content clear-block']//div[@class = 'field-item odd']/p/text()")
                t += doc1.xpath("//div[@class ='content clear-block']/p/text()")
                txt = ','.join([x.strip() for x in t if x.strip()])

                inf[3].append(txt)
                inf[4].append(str(olevsk().get_name()))
            except Exception as ex:
                print(ex)
            continue
        return inf
if __name__ == '__main__':
        date_load = date.today()
        dT = str(date_load.strftime('%Y%m%d'))
        dT = '20170620'
        m = olevsk.run(0,dT)
        pass
