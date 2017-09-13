
from lxml.html import fromstring
import htmlmov
from datetime import date
from urllib.request import urlparse
from editsqlite import *

month = {"Січень":"01","Лютий":"02","Березень":"03","Квітень":"04","Травень":"05","Червень":"06",
         "Липень":"07","Серпень":"08","Вересень":"09","Жовтень":"10","Литопад":"11","Грудень":"12",}
class mnzt:
    def get_name(self):
        return 'Малин'

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
        dT = str(dT).replace("-", '')
        cur.execute(
            "SELECT link FROM main "
            "WHERE ({0}) and date between {1} AND {2} ".format("domain = '{0}'".format("Малин"),
                                                               int(dT) * 10000, int(dT) * 10000 + 9999))
        check_list = cur.fetchall()
        con.close()
        return check_list

    def run(self, dT):

        duplicate = self.check_on_duplicate(dT)
        hrf = []
        j = 1
        #лічільник(перевіряє чи наявна небхідна дата на сторінці
        znak = 0
        # парсинг перших 4-ох сторінок
        while j < 5:
            try:
                url = 'http://mn.zt.ua/category/novyny-malyna/page/{0}/'.format(j)
                # Завантажуємо код сторінки
                page = htmlmov.url_line(url)
                doc = fromstring(page)
                doc.make_links_absolute(url)
                # Заванажуємо посилання повідовлень за зазначену дату
                ref_news = doc.xpath("//ul[@class = 'entry-list clearfix']//header/h6/a")
                dat = doc.xpath(
                    '//ul[@class = "entry-list clearfix"]//header//span[@class = "date updated"]/text()')
                hrf += [ref_news[x].get("href") for x in range(ref_news.__len__()) if
                        dat[x][-4:] + month[str(dat[x][:-8]).replace(" ", '')] + dat[x][-8:-6].replace(" ", '0') == dT]
                if not not hrf:
                    znak+=1
                if znak >1:
                    break
                j+=1
                pass
            except Exception as ex:
                print(ex)
        kol = len(hrf)
        i = 0
        while i < kol:
            for j in range(len(duplicate)):
                if hrf[i] == duplicate[j][0]:
                    hrf.pop(i)
                    kol -= 1
            i += 1
        inf = [[],[],[],[],[]]
        for x in hrf:
            try:
                page1 = htmlmov.url_line(x)
                doc1 = fromstring(page1)
                doc1.make_links_absolute(x)
                #Заповлення масиву даними
                inf[0].append(x)
                inf[1].append(dT+'0000')
                inf[2].append(doc1.xpath('//h1/text()')[0])

                t = doc1.xpath("//div[@class = 'entry-content clearfix']//p/text()")
                txt = ','.join([x.strip() for x in t if x.strip()])

                inf[3].append(txt)
                inf[4].append(str(mnzt().get_name()))
            except Exception as ex:
                print(ex)
            continue
        return inf

if __name__ == '__main__':
        date_load = date.today()
        dT = str(date_load.strftime('%Y%m%d'))
        dT = '20170611'
        m = mnzt().run(dT)
        pass