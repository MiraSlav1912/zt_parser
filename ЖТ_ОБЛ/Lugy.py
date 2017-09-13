from lxml.html import fromstring
import htmlmov
from datetime import date
from urllib.request import urlparse
import sqlite3

Month = {"січня":"01","лютого":"02","березня":"03","квітня":"04","травня":"05","червня":"06",
         "липня":"07","серпня":"08","вересня":"09","жовтня":"10","литопада":"11","грудня":"12",}

class lugyny:
    def get_name(self):
        return 'Лугини'

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
            "WHERE ({0}) and date between {1} AND {2} ".format("domain = '{0}'".format(lugyny().get_name()),
                                                               int(dT) * 10000, int(dT) * 10000 + 9999))
        check_list = cur.fetchall()
        con.close()
        return check_list

    def run(self,dT):
        hrf = []
        url = 'http://lugini-rayrada.zt.gov.ua/index.php/novyny/novini-rajonu?start={0}0'
        chek_list = lugyny().check_on_duplicate(dT)
        dat = []
        j = 0
        while j < 5:
            try:
                url.format(j)
                # Завантажуємо код сторінки
                page = htmlmov.url_line(url)
                doc = fromstring(page)
                doc.make_links_absolute(url)

                ref_news = doc.xpath("//div[@class = 'contentpaneopen']/h2/a")
                dat = doc.xpath(
                    "//div[@class = 'article-tools clearfix']//dd[@class = 'published']/text()")

                dat = [dat[x][-6:-2]+Month[str(dat[x][20:-7])]+dat[x][17:19] for x in range(dat.__len__())]
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
                inf[1].append(dT+"0000")

                inf[2].append(doc1.xpath("//h2/a/text()"))
                t = []
                t += doc1.xpath("//div[@class = 'item-page']/p//text()")
                txt = ','.join([x.strip().replace('\xa0','') for x in t if x.strip()])

                inf[3].append(txt)
                inf[4].append(str(lugyny().get_name()))
            except Exception as ex:
                print(ex)
            continue
        return inf
if __name__ == '__main__':
        date_load = date.today()
        dT = str(date_load.strftime('%Y%m%d'))
        dT = '20170623'
        m = lugyny().run(dT)
        pass
