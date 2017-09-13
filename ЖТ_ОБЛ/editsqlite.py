__author__ = 'Myroslav'

import sqlite3
from tkinter import ttk,messagebox
from zhzh_info import *
from ZhytInfo import *
from rioberdychivinfo import *
from berdichevbiz import *
from zerofourone import *
from korosten import *
from Ovruch import *
from Malyn import *
from olevsk import *
from Lugy import *

class Working_with_BD:

    def __init__(self,choise,date):
        # self.date_load = date.today()
        # self.dT = str(self.date_load.strftime('%Y-%m-%d'))
        self.date = date
        self.choise = choise
        self.name_db = 'All_Pars_BD.db3'
        self.con = sqlite3.connect(self.name_db)
        self.cur = self.con.cursor()

        dd = self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='main'").fetchone()
        if not dd:
            self.cur.execute('''CREATE TABLE main
                            ( link text,date integer, title text, body text, domain text)''')

    def read(self):
        if self.choise != '':
            self.cur.execute(
                "SELECT link, date, title, body, domain FROM main "
                "WHERE ({0}) and date between {1} AND {2} "
                "ORDER BY date DESC".format('Null ' + self.choise, int(self.date[0]) * 10000,
                                            int(self.date[-1]) * 10000 + 9999))
        return self.cur.fetchall()
        self.con.close()

    def search(self,key):
        if self.choise != '':
            key2=""
            # if '+' in key:
            #     key2 = str(key).replace(" ", "").split('+')
            #     key2 = ['AND (body LIKE "%{0}%")'.format(x) for x in key2]
            #     key2 = ",".join(key2).replace(',','')
            #     key = ""

            self.cur.execute(
                "SELECT link, date, title, body, domain FROM main "
                "WHERE ({0}) and date between {1} AND {2} "
                "AND {3}"
                "ORDER BY date DESC".format('Null ' + self.choise, int(self.date[0]) * 10000,
                                            int(self.date[-1]) * 10000 + 9999,
                '(body LIKE "%{0}%")'.format(key)))

        return self.cur.fetchall()

    def write(self):
        if self.choise == 'Житомир':
            zhzh_date = self.date[:4]+"-"+self.date[4:6]+"-"+self.date[-2:]
            self.inf = zhzh_info.run(0,zhzh_date)
            m = www_zhitomir_info.run(0, self.date)
            for i in range(5):
                self.inf[i] += m[i]

        if self.choise == 'Бердичів':
            self.inf =  rio_berdichev.run(0,self.date)
            m = berdichev_biz.run(0, self.date)
            for i in range(5):
                self.inf[i] += m[i]

        if self.choise == 'Коростень':
            self.inf = www_korosten.run(0, self.date)

        if self.choise == 'Новоград_Волинський':
            self.inf = zerofourone.run(0, self.date)

        if self.choise == 'Овруч':
            self.inf = ovruch.run(0, self.date)

        if self.choise == 'Малин':
            self.inf = mnzt().run(self.date)

        if self.choise == 'Олевськ':
            self.inf = olevsk().run(self.date)

        if self.choise == 'Лугини':
            self.inf = lugyny().run(self.date)
        pass
        [self.cur.execute("INSERT INTO main ( link, date, title, body, domain) "
                          "VALUES (?, ?, ?, ?, ?)",
                         (self.inf[0][i], self.inf[1][i], self.inf[2][i], self.inf[3][i],self.inf[4][i]))
                        for i in range(self.inf[0].__len__())]

        self.con.commit()
        self.con.close()

    def check_on_duplicate(self):
        dd = self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='main'").fetchone()
        if not dd:
            return ''
        self.cur.execute(
            "SELECT link FROM main "
            "WHERE ({0}) and date between {1} AND {2} ".format("domain = '{0}'".format(self.choise),
                                                               int(self.date) * 10000, int(self.date) * 10000 + 9999))
        check_list = self.cur.fetchall()
        self.con.close()
        return check_list

if __name__ == '__main__':
    m = Working_with_BD('Лугини','20170622').write()
    pass







