#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from datetime import date, datetime
#import time

class Calendar_mov(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.cur_t = date.today()
        self.d = []
        self.make_widg()
        self.load_month(self.cur_t)
        self.parent = parent

    def make_widg(self):
        w = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд']
        for j in range(7):
            fg = 'black' if j < 5 else 'red'
            ttk.Label(self, text=w[j], foreground=fg).grid(row=1, column=j)
        b1 = ttk.Label(self, text='<')
        b1.grid(row=0, column=0)
        b1.bind('<Button-1>', self.dwn)
        b2 = ttk.Label(self, text='>')
        b2.grid(row=0, column=6)
        b2.bind('<Button-1>', self.dwn)
        self.d.append(ttk.Label(self, text=''))
        self.d[0].grid(row=0, column=1, columnspan=5)
        r, c = 2, 0
        for dt in range(1, 43):
            fg = 'black' if c < 5 else 'red'
            self.d.append(ttk.Label(self, text='', width=3,
                                    foreground=fg, relief='raised'))
            self.d[dt].grid(row=r, column=c)
            self.d[dt].bind('<Button-1>', self.sd)
            if c == 6:
                r, c = r + 1, 0
            else:
                c += 1

    def load_month(self, t):
        mn = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень',
              'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень']
        c = t.replace(day=1).weekday()
        if t.month == 12:
            n_day = (t.replace(year=t.year + 1, month=1, day=1) - t.replace(day=1)).days
        else:
            n_day = (t.replace(month=t.month + 1, day=1) - t.replace(day=1)).days
        self.d[0]['text'] = '{0} {1}'.format(mn[t.month - 1], t.year)
        r = 2
        for dt in range(1, n_day + 1):
            self.d[dt + c]['text'] = ' {0:02d} '.format(dt)

    def dwn(self, event):
        for dt in range(43):
            self.d[dt]['text'] = ''
        if event.widget['text'] == '<':
            if self.cur_t.month == 1:
                curnt = self.cur_t.replace(year=self.cur_t.year - 1, month=12)
            else:
                curnt = self.cur_t.replace(month=self.cur_t.month - 1)
        else:
            if self.cur_t.month == 12:
                curnt = self.cur_t.replace(year=self.cur_t.year + 1, month=1)
            else:
                curnt = self.cur_t.replace(month=self.cur_t.month + 1)
        self.cur_t = curnt
        self.load_month(curnt)

    def sd(self, event):
        try:
            day_ = int(event.widget['text'])
        except:
            ...
        else:
            #self.cur_t = self.cur_t.replace(day=day_)
            self.cur_t = self.cur_t.replace(day=day_)
            self.parent.destroy()

#cur_t = time.localtime()
d = []
cur_ = date.today()


def strDiso2dt(s):
    try:
        y, m, d = s.strip().split('-')
    except:
        return None
    return date(int(y), int(m), int(d))

def strTiso2dt(s):
    try:
        y, m, d = [int(x) for x in s[:10].split('-')]
        h, mm = [int(x) for x in s[11:16].strip().split(':')]
    except:
        return None
    return datetime(y, m, d, h, mm)

def main():
    # Calendar_mov().mainloop()
    #gui()
    d = strDiso2dt('2014-03-15')
    print(type(d))

#def dwn(event):
#global d, cur_
#for dt in range(43):
#d[dt]['text']=''
#if event.widget['text'] == '<':
#if cur_.month == 1:
#cur_ = cur_.replace(year=cur_.year-1,month=12)
#else:
#cur_ = cur_.replace(month=cur_.month-1)
#else:
#if cur_.month == 12:
#cur_ = cur_.replace(year=cur_.year+1,month=1)
#else:
#cur_ = cur_.replace(month=cur_.month+1)
#month_load(cur_)
#def month_load(t):
#global cur_, d
#mn =['Січень','Лютий','Березень','Квітень','Травень','Червень',
#'Липень','Серпень','Вересень','Жовтень','Листопад','Грудень']
#c = t.replace(day=1).weekday()
#if t.month ==12:
#n_day = (t.replace(year=t.year+1,month=1,day=1)-t.replace(day=1)).days
#else:
#n_day = (t.replace(month=t.month+1,day=1)-t.replace(day=1)).days
#d[0]['text']='{0} {1}'.format(mn[t.month-1],t.year)
#r = 2
#for dt in range(1,n_day+1):
#d[dt+c]['text']=' {0:02d} '.format(dt)
#def sd(event):
#global cur_
#try:
#day_ = int(event.widget['text'])
#except:
#...
#else:
#cur_ = cur_.replace(day=day_)
#print(cur_)
#def gui():
#global tk3,d
#w=['Пн','Вт','Ср','Чт','Пт','Сб','Нд']
#tk3=Tk()
#tk3.title('Календар')
#for j in range(7):
#fg = 'black' if j <5 else 'red'
#ttk.Label(text=w[j],foreground=fg).grid(row=1,column=j)
#b1 = ttk.Label(text='<')
#b1.grid(row=0,column=0)
#b1.bind('<Button-1>',dwn)
#b2 = ttk.Label(text='>')
#b2.grid(row=0,column=6)
#b2.bind('<Button-1>',dwn)
#d.append(ttk.Label(text=''))
#d[0].grid(row=0,column=1,columnspan=5)
#r,c = 2,0
#for dt in range(1,43):
#fg = 'black' if c <5 else 'red'
#d.append(ttk.Label(text='', width=3,foreground=fg,relief='raised'))
#d[dt].grid(row=r,column=c)
#d[dt].bind('<Button-1>', sd)
#if c == 6:
#r, c = r+1,0
#else:
#c +=1
#month_load(cur_)

if __name__ == '__main__':
    main()
    #tk3.mainloop()
