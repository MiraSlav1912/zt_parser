__author__ = 'Myroslav'

from lxml.html import fromstring
import htmlmov
from datetime import date,timedelta
from urllib.request import urlparse
import sqlite3

class zerofourone:
    def get_name(self):
        return 'Новоград Волинський'

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
            "WHERE ({0}) and date between {1} AND {2} ".format("domain = '{0}'".format(zerofourone.get_name(0)), int(dT) * 10000, int(dT) * 10000 + 9999))
        check_list = cur.fetchall()
        con.close()
        return check_list
    def run(self, dT):
        hrf = []
        dat = []
        url = 'http://www.04141.com.ua/news/date/{0}'#2017-02-09

        try:
            #Завантажуємо код сторінки
            ddT = dT[:4] + '-' + dT[4:6] + '-' + dT[-2:]
            url_ = url.format(ddT)
            page = htmlmov.url_line(url_)
            doc = fromstring(page)
            doc.make_links_absolute(url_)
            #Заванажуємо посилання повідовлень за зазначену дату
            ref_news = doc.xpath("//div[@class = 'card__title']/a")
            hrf += [ref_news[x].get("href") for x in range(ref_news.__len__())]
            chek_list = zerofourone.check_on_duplicate(0, dT)
            [hrf.remove(j) for i in chek_list for j in hrf if i[0] == j]
            d = doc.xpath("//div[@class = 'date']/span/text()")
            dat += [d[x][:5].replace(":", '') for x in range(len(hrf))]

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
                k = '{0}{1}'.format(dT,dat[i])
                i+=1
                inf[1].append(k)
                inf[2].extend(doc1.xpath('//div[@class="title-container inner-title"]/h1/text()'))

                t = doc1.xpath('//div[@class="article-text"]//text()')
                txt = ','.join([x.strip() for x in t if x.strip()])

                # if txt =='':
                #     tt = doc1.xpath('//div[@class="article-text"]//p[@style = "text-align: justify;"]/text()')
                #     txt += ','.join([x.strip() for x in tt if x.strip()])
                inf[3].append(txt)
                inf[4].append(str(zerofourone.get_name(0)))
            except Exception as ex:
                print(ex)
            continue
        return inf

if __name__ == '__main__':
        date_load = date.today()
        dT = str(date_load.strftime('%Y%m%d'))
        m = zerofourone.run(0,dT)
        pass