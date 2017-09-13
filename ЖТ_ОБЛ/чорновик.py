__author__ = 'Myroslav'
import sqlite3
dT = 20170527

import urllib.request
import re

site = urllib.request.urlopen('http://mistaua.com/%D0%9D%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8/%D0%9F%D0%BE%D0%B4%D1%96%D1%97/%D0%BF%D1%96%D1%80%D0%BE%D1%82%D0%B5%D1%85%D0%BD%D1%96%D0%BA%D0%B8-%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%96-%D0%B7%D0%BD%D0%B8%D1%89%D0%B8%D0%BB%D0%B8-4/81635/?setcity=320')
html = site.read().decode('utf8')

print(html)
txt = re.findall()


"r'<h[1-2][^>]*><a[^>]*>(.*?)</a></h[1-2]>'"

"среди заголовков h1 и h2 с любыми классами и id внутри которых содержится ссылка, так же с любыми классами и id получи текст"
# n = int(input('Введіть кількість камнів '))
# w = []
# for i in range(n):
#     w.append(input('Вага {0} камня '.format(i+1)))
#
# w.sort()
#
# box1,box2 = 0,0
# box1 = int(w[::-1][0])
#
# for i in range(n-1):
#     g = w[::-1][i + 1]
#     if box1 ==box2:
#         box1 = box1 + int(w[::-1][i + 1])
#         continue
#     if box1 > box2:
#         box2 = box2 + int(w[::-1][i+1])
#     if box2 > box1:
#         box1 = box1 + int(w[::-1][i+1])
#
# print('box1 = {0} \nbox2 = {1}'.format(box1,box2))
# if box2 > box1:
#     print(box2-box1)
# else:
#     print(box1-box2)


# class Lol:
#     def __init__(self,name):
#         self.name  = name
#         self.get_name()
#     def get_name(self):
#         return print(self.name)
#
# m = Lol("Мирось")
#
# m= [1,2,3,4,5,6]
# n = [2,3,4,8,0,9,8,2]
#
# kol = len(m)
# i=0
# while i < kol:
#     for j in range(len(n)):
#         if m[i] == n[j]:
#             m.pop(i)
#             kol-=1
#     i+=1
# print(m)
# choise = []
#             for k, v in globall.items():
#                 if v == True:
#                     choise.append('or domain = "{0}"'.format(k))
#             c = ' '.join([x.strip() for x in choise if x.strip()])
#



# LISTBOX
# from tkinter import *
#
# root = Tk()
#
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
#
# listbox = Listbox(root)
# listbox.pack()
#
# for i in range(100):
#     listbox.insert(END, i)
#
# # attach listbox to scrollbar
# listbox.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)
#
# mainloop()



#PROGRESS BAR
# import tkinter as tk
# from tkinter import ttk
#
#
# class SampleApp(tk.Tk):
#
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         self.button = ttk.Button(text="start", command=self.start)
#         self.button.pack()
#         self.progress = ttk.Progressbar(self, orient="horizontal",
#                                         length=200, mode="determinate")
#         self.progress.pack()
#
#         self.bytes = 0
#         self.maxbytes = 0
#
#     def start(self):
#         self.progress["value"] = 0
#         self.maxbytes = 50000
#         self.progress["maximum"] = 50000
#         self.read_bytes()
#
#     def read_bytes(self):
#         '''simulate reading 500 bytes; update progress bar'''
#         self.bytes += 500
#         self.progress["value"] = self.bytes
#         if self.bytes < self.maxbytes:
#             # read more bytes after 100 ms
#             self.after(100, self.read_bytes)
#
# app = SampleApp()
# app.mainloop()

# root = Tk()
# globall = {'Житомир':False,'oval1':False,'oval2':False}
#
# class Constructor:
#     def __init__(self):
#         self.lol()
#     def lol(self):
#         self.buttom1= Button(root,text = "Завантаження",width = 20,bg = 'gray45')
#         self.buttom1.pack(side='top')
#         self.canvas = Canvas(root, width=533, height=695)
#         self.canvas.pack()
#         self.im = Image.open("zh.jpg")
#         self.cropped = self.im.crop((0, 0, 533, 695))
#         self.tk_im = ImageTk.PhotoImage(self.cropped)
#
#
#
#     def myEvent(self,event,tag):
#         self.canvas.itemconfig('{0}'.format(tag),fill="red")
#         globall[tag] = True
#         print(globall[tag])
#     def myEvent2(self,event,tag):
#         self.canvas.itemconfig('{0}'.format(tag),fill='tan',)
#         globall[tag] = False
#         print(globall[tag])
#
#
#     def real(self,event):
#         print(globall['Житомир'])
#
# # canvas.create_arc([250,230],[320,330],start=0,extent=140,
# #           style=CHORD,fill="green")
# # canvas.create_arc([340,230],[410,330],start=0,extent=140,
# #           style=ARC,outline="darkgreen",width=2)
# if __name__ == '__main__':
#     k = Constructor()
#     root.mainloop()
#CHECK BUTTON
# self.frame2 = Frame(self.frame_one,bg='gray50', bd=5)
# self.frame2.pack(side="right", fill='both', expand=True)

# Label(self.frame2,text="Вибір регіону",bg = 'gray60').grid(row=0, column=0, sticky=W)
# self.aktivator_66 = StringVar()
# self.chek66 = Checkbutton(self.frame2, text='Все', width=20, variable=self.aktivator_66, bg=gray,onvalue="10")
# self.chek66.grid(row=1, column=0, sticky='w')
# self.chek66.deselect()
#
# self.chek1 = Checkbutton(self.frame2,text = 'BIZ-Бердичів', width=20,variable = self.aktivator_1,bg = gray,onvalue="2sfsdfsd")
# self.chek1.grid(row=2, column= 0, sticky = W)
# self.chek1.deselect()
#
# self.aktivator_2 = StringVar()
# self.chek2 = Checkbutton(self.frame2, text='ЖЖ інфо', width=20, variable=self.aktivator_2, bg=gray, onvalue="3sdfsdfsdf")
# self.chek2.grid(row = 3, column = 0,sticky = W)
# self.chek2.deselect()
