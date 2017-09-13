__author__ = 'Myroslav'

from tkinter import *
from editsqlite import *
from datetime import date
import date_,append_date

gray = 'gray70'
date_load = date.today()
dT = str(date_load.strftime('%Y-%m-%d'))
globall = {'Житомир':False,'Олевськ':False,'Овруч':False,'Лугини':False,'Народичі':False,'Коростень':False,
           'Ємільчине':False,'Малин':False,'Новоград_Волинський':False,'Хорошів':False
    , 'Червоноамійськ': False,'Баранівка':False,'Радомишиль':False,'Дзержинськ':False,'Любар':False,'Чуднів':False,
           'Бердичів':False,'Андрушівка':False,'Коростень':False,'Попільня':False,'Ружин':False,'Коростишів':False
    , 'Черняхів': False, 'Брусилів' : False}
region = {'Житомир' : 'or domain = "Журнал Житомира" or domain = "Житомир Інфо"',
          'Бердичів': 'or domain = "РІО Бердичів" or domain = "Бердичів BIZ"',
          'Коростень': 'or domain = "Новини Коростеня"',
          'Новоград_Волинський':'or domain = "Новоград Волинський"',
          'Овруч':'or domain = "Овруч"',
          'Малин':'or domain = "Малин"',}
# print(len(globall.keys()),globall.keys())

class Constructors:
    def __init__(self):

        self.nb = ttk.Notebook(root)
        self.frame_one = Frame(self.nb)
        self.frame_two = Frame(self.nb)
        self.nb.add(self.frame_two, text="Карта")
        self.nb.add(self.frame_one, text="Дані")
        self.nb.pack()
        #створення інтерфейсу
        self.map_of_choise()
        self.data()

        self.buttom1.bind("<Button-1>", self.vybir_regionu)
        self.buttom2.bind("<Button-1>", self.search)
        self.buttom3.bind("<Button-1>", self.write)

    def map_of_choise(self):
        # КАРТА
        self.frame21 = Frame(self.frame_two)
        self.frame21.pack()

        self.canvas1 = Canvas(self.frame_two, width=533, height=695, bg='khaki3')
        self.canvas1.pack()

        # self.im = Image.open("zh.jpg")
        # self.cropped = self.im.crop((0, 0, 533, 695))
        # self.tk_im = ImageTk.PhotoImage(self.cropped)
        # self.canvas1.create_image(266, 347, image=self.tk_im)

        self.canvas1.create_polygon(219, 453, 260, 421, 336, 440, 358, 481, 316, 517, 252, 517, 220, 490, tags='Житомир',
                                   fill='khaki', )
        self.canvas1.tag_bind('Житомир', "<Button-3>", lambda event, tag='Житомир': self.myEvent(event, tag))
        self.canvas1.tag_bind('Житомир', "<Button-1>", lambda event, tag='Житомир': self.myEvent2(event, tag))

        self.canvas1.create_polygon(55, 172, 94, 57, 206,34,190,189,tags='Олевськ', fill='khaki', )
        self.canvas1.tag_bind('Олевськ', "<Button-3>", lambda event, tag='Олевськ': self.myEvent(event, tag))
        self.canvas1.tag_bind('Олевськ', "<Button-1>", lambda event, tag='Олевськ': self.myEvent2(event, tag))

        self.canvas1.create_polygon(204,122, 212, 33,340,20,447,80,341,176, tags='Овруч', fill='khaki', )
        self.canvas1.tag_bind('Овруч', "<Button-3>", lambda event, tag='Овруч': self.myEvent(event, tag))
        self.canvas1.tag_bind('Овруч', "<Button-1>", lambda event, tag='Овруч': self.myEvent2(event, tag))

        self.canvas1.create_polygon(203,132,338,182,237,246,198,191, tags='Лугини', fill='khaki', )
        self.canvas1.tag_bind('Лугини', "<Button-3>", lambda event, tag='Лугини': self.myEvent(event, tag))
        self.canvas1.tag_bind('Лугини', "<Button-1>", lambda event, tag='Лугини': self.myEvent2(event, tag))

        self.canvas1.create_polygon(348,184,446,90,470,225,399,220, tags='Народичі', fill='khaki', )
        self.canvas1.tag_bind('Народичі', "<Button-3>", lambda event, tag='Народичі': self.myEvent(event, tag))
        self.canvas1.tag_bind('Народичі', "<Button-1>", lambda event, tag='Народичі': self.myEvent2(event, tag))

        self.canvas1.create_polygon(237,256,342,191,394,226,334,304,233,292, tags = 'Коростень', fill = 'khaki', )
        self.canvas1.tag_bind('Коростень', "<Button-3>", lambda event, tag='Коростень': self.myEvent(event, tag))
        self.canvas1.tag_bind('Коростень', "<Button-1>", lambda event, tag='Коростень': self.myEvent2(event, tag))

        self.canvas1.create_polygon(54,185,192,204,228,252,222,332,100,300, tags = 'Ємільчине', fill = 'khaki', )
        self.canvas1.tag_bind('Ємільчине', "<Button-3>", lambda event, tag='Ємільчине': self.myEvent(event, tag))
        self.canvas1.tag_bind('Ємільчине', "<Button-1>", lambda event, tag='Ємільчине': self.myEvent2(event, tag))

        self.canvas1.create_polygon(340,310,400,231,470,238,500,320,430,333, tags = 'Малин', fill = 'khaki', )
        self.canvas1.tag_bind('Малин', "<Button-3>", lambda event, tag='Малин': self.myEvent(event, tag))
        self.canvas1.tag_bind('Малин', "<Button-1>", lambda event, tag='Малин': self.myEvent2(event, tag))

        self.canvas1.create_polygon(45,190,92,310,190,334,155,392,30,373, tags = 'Новоград_Волинський', fill = 'khaki', )
        self.canvas1.tag_bind('Новоград_Волинський', "<Button-3>", lambda event, tag='Новоград_Волинський': self.myEvent(event, tag))
        self.canvas1.tag_bind('Новоград_Волинський', "<Button-1>", lambda event, tag='Новоград_Волинський': self.myEvent2(event, tag))

        self.canvas1.create_polygon(231,336,235,300,334,313,262,404, tags = 'Хорошів', fill = 'khaki', )
        self.canvas1.tag_bind('Хорошів', "<Button-3>", lambda event, tag='Хорошів': self.myEvent(event, tag))
        self.canvas1.tag_bind('Хорошів', "<Button-1>", lambda event, tag='Хорошів': self.myEvent2(event, tag))

        self.canvas1.create_polygon(162,400,200,337,230,342,257,412,216,444, tags = 'Червоноамійськ', fill = 'khaki', )
        self.canvas1.tag_bind('Червоноамійськ', "<Button-3>", lambda event, tag='Червоноамійськ': self.myEvent(event, tag))
        self.canvas1.tag_bind('Червоноамійськ', "<Button-1>", lambda event, tag='Червоноамійськ': self.myEvent2(event, tag))

        self.canvas1.create_polygon(354,322,430,340,490,330,471,415,445,443, tags = 'Радомишиль', fill = 'khaki', )
        self.canvas1.tag_bind('Радомишиль', "<Button-3>", lambda event, tag='Радомишиль': self.myEvent(event, tag))
        self.canvas1.tag_bind('Радомишиль', "<Button-1>", lambda event, tag='Радомишиль': self.myEvent2(event, tag))

        self.canvas1.create_polygon(95,505,87,446,175,423,211,452,212,489,161,487, tags = 'Дзержинськ', fill = 'khaki', )
        self.canvas1.tag_bind('Дзержинськ', "<Button-3>", lambda event, tag='Дзержинськ': self.myEvent(event, tag))
        self.canvas1.tag_bind('Дзержинськ', "<Button-1>", lambda event, tag='Дзержинськ': self.myEvent2(event, tag))

        self.canvas1.create_polygon(27,380,155,402,171,417,72,440, tags = 'Баранівка', fill = 'khaki', )
        self.canvas1.tag_bind('Баранівка', "<Button-3>", lambda event, tag='Баранівка': self.myEvent(event, tag))
        self.canvas1.tag_bind('Баранівка', "<Button-1>", lambda event, tag='Баранівка': self.myEvent2(event, tag))

        self.canvas1.create_polygon(68,553,101,511,158,497,133,600,110,608, tags = 'Любар', fill = 'khaki', )
        self.canvas1.tag_bind('Любар', "<Button-3>", lambda event, tag='Любар': self.myEvent(event, tag))
        self.canvas1.tag_bind('Любар', "<Button-1>", lambda event, tag='Любар': self.myEvent2(event, tag))

        self.canvas1.create_polygon(140,598,168,493,217,496,244,521,205,597, tags = 'Чуднів', fill = 'khaki', )
        self.canvas1.tag_bind('Чуднів', "<Button-3>", lambda event, tag='Чуднів': self.myEvent(event, tag))
        self.canvas1.tag_bind('Чуднів', "<Button-1>", lambda event, tag='Чуднів': self.myEvent2(event, tag))

        self.canvas1.create_polygon(212,598,247,529,305,523,338,580, tags = 'Бердичів', fill = 'khaki', )
        self.canvas1.tag_bind('Бердичів', "<Button-3>", lambda event, tag='Бердичів': self.myEvent(event, tag))
        self.canvas1.tag_bind('Бердичів', "<Button-1>", lambda event, tag='Бердичів': self.myEvent2(event, tag))

        self.canvas1.create_polygon(319,526,361,490,417,518,408,581,353,588, tags = 'Андрушівка', fill = 'khaki', )
        self.canvas1.tag_bind('Андрушівка', "<Button-3>", lambda event, tag='Андрушівка': self.myEvent(event, tag))
        self.canvas1.tag_bind('Андрушівка', "<Button-1>", lambda event, tag='Андрушівка': self.myEvent2(event, tag))

        self.canvas1.create_polygon(367,484,342,437,375,379,440,450,423,512, tags = 'Коростишів', fill = 'khaki', )
        self.canvas1.tag_bind('Коростишів', "<Button-3>", lambda event, tag='Коростишів': self.myEvent(event, tag))
        self.canvas1.tag_bind('Коростишів', "<Button-1>", lambda event, tag='Коростишів': self.myEvent2(event, tag))

        self.canvas1.create_polygon(448,453, 478, 419, 501, 493, 430, 510,tags='Брусилів', fill='khaki', )
        self.canvas1.tag_bind('Брусилів', "<Button-3>", lambda event, tag='Брусилів': self.myEvent(event, tag))
        self.canvas1.tag_bind('Брусилів', "<Button-1>", lambda event, tag='Брусилів': self.myEvent2(event, tag))

        self.canvas1.create_polygon(264,414,341,319,370,370,335,432, tags = 'Черняхів', fill = 'khaki', )
        self.canvas1.tag_bind('Черняхів', "<Button-3>", lambda event, tag='Черняхів': self.myEvent(event, tag))
        self.canvas1.tag_bind('Черняхів', "<Button-1>", lambda event, tag='Черняхів': self.myEvent2(event, tag))

        self.canvas1.create_polygon(416,584,424,521,505,498,514,571,459,610, tags = 'Попільня', fill = 'khaki', )
        self.canvas1.tag_bind('Попільня', "<Button-3>", lambda event, tag='Попільня': self.myEvent(event, tag))
        self.canvas1.tag_bind('Попільня', "<Button-1>", lambda event, tag='Попільня': self.myEvent2(event, tag))

        self.canvas1.create_polygon(315,597,410,589,458,618,466,630,359,630, tags = 'Ружин', fill = 'khaki', )
        self.canvas1.tag_bind('Ружин', "<Button-3>", lambda event, tag='Ружин': self.myEvent(event, tag))
        self.canvas1.tag_bind('Ружин', "<Button-1>", lambda event, tag='Ружин': self.myEvent2(event, tag))

        Label(self.frame21, text="з", bg=gray).pack(side="left")
        self.date_start = date_.sel_date(self.frame21)
        self.date_start.pack(side="left")

        Label(self.frame21, text="по", bg=gray).pack(side="left")
        self.date_end = date_.sel_date(self.frame21)
        self.date_end.pack(side="left")

        #dd = self.date_start.get_date().strftime("%Y-%m-%d")# %H:%M" ) зчитування даних
        # self.date_start.get_date().strptime(line_date,"%Y-%m-%d %H:%M")# зі строчки конвертує в тип
        # dd = self.date_start.get_date()-datetime.timedelta(hours = 1) віднімання однієї години від дати (російські сайти!!!)

        self.buttom3 = Button(self.frame21, text="Оновлення БД", width=20, bg='gray45')
        self.buttom3.pack(side="left")
    #збір новин
    def write(self,event):
            self.dat_now()
            if globall['Житомир'] == True:
                self.colecting_DB('Житомир')
            if globall['Бердичів'] == True:
                self.colecting_DB('Бердичів')
            if globall['Коростень'] == True:
                self.colecting_DB('Коростень')
            if globall['Новоград_Волинський'] == True:
                self.colecting_DB('Новоград_Волинський')
            if globall['Овруч'] == True:
                self.colecting_DB('Овруч')
            if globall['Малин'] == True:
                self.colecting_DB('Малин')
            return self.dat

    #Зчитування з бази даних відомостей про новини регіону
    def colecting_DB(self,region):
        da = []
        for i in range(len(self.dat)):
            Working_with_BD(region, self.dat[i]).write()
        return  da

    def data(self):
        # ДАНІ
        self.frame12 = Frame(self.frame_one)
        self.frame12.pack()

        self.frame1 = Frame(self.frame_one, bg='gray50', bd=5)
        self.frame1.pack(fill='both',expand = YES)

        self.text2 = Text(self.frame1, height=1, width=60, font='Arial 14', wrap=WORD)
        self.text2.pack(fill='x')

        self.buttom1 = Button(self.frame12, text="Завантаження", width=20, bg='gray45')
        self.buttom1.pack(side="left")
        self.buttom2 = Button(self.frame12, text="Пошук", width=20, bg='gray45')
        self.buttom2.pack(side="left")

        self.text1 = Text(self.frame1, font='Arial 14', height=95, width=60, bg='gray90')

        scrollbar = Scrollbar(self.text1)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.text1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text1.yview)

        self.text1.tag_configure('title', font='bold', foreground='red')
        self.text1.pack(fill='both',expand = YES)
    #Інформація про вибрану дату
    def dat_now(self):
        start = self.date_start.get_date().strftime("%Y%m%d")  # %H:%M" ) зчитування даних
        end = self.date_end.get_date().strftime("%Y%m%d")  # %H:%M" ) зчитування даних
        self.dat = append_date.append_date(start, end)
        if self.dat == 'Помилка вводу':
            return messagebox.showinfo("Помилка", "Помилка вибору дати")
        else:
            return self.dat
    #Зміна кольору при натисканні на регіон
    def myEvent(self,event,tag):
        self.canvas1.itemconfig('{0}'.format(tag),fill="red")
        globall[tag] = True
        print(globall[tag])
    def myEvent2(self,event,tag):
        self.canvas1.itemconfig('{0}'.format(tag),fill='tan',)
        globall[tag] = False
        print(globall[tag])

    #Інформація про вибрані регіони
    def choised_region(self):
        choise = [region[x] for x in globall if globall[x] == True]

        choise = ','.join([x.strip() for x in choise if x.strip()]).replace(",", '')
        return choise

    def vybir_regionu(self,event):
        try:
            #Відображення вибраних регіонів
            self.mass = []
            canvas = []
            self.mass.append(Working_with_BD(self.choised_region(),self.dat_now()).read())
            self.text1.delete(1.0, END)
            for i in range(len(self.mass[0])):
                canvas.append(Canvas(width=510, height=65, bg='lightblue', ))
                canvas[i].create_text(10, 13, text=self.mass[0][i][4], font="Calibry", fill='dimgray', anchor="w")
                Date = str(self.mass[0][i][1])[8:10] + ':' + str(self.mass[0][i][1])[10:12] + ' ' + str(
                    self.mass[0][i][1])[6:8] + '-' + str(self.mass[0][i][1])[4:6] + '-' + str(self.mass[0][i][1])[0:4]
                canvas[i].create_text(350, 13, text=Date, font="Calibry", fill='gray', anchor="w")
                canvas[i].create_text(10, 40, width=510, text=self.mass[0][i][2], font="Calibry", fill='indigo',
                                           anchor="w")
                self.text1.window_create(CURRENT, window=canvas[i])
                canvas[i].bind("<Double-Button-1>", lambda event, i=i: self.create_new_pole(event, i))
        except IndexError :
            messagebox.showinfo("Помилка", "Виберіть район")


    def create_new_pole(self,event,i):
        root2 = Tk()
        self.text2 = Text(root2, height=30, width=70, font='Arial 14', wrap=WORD)
        self.text2.pack(side='top', fill='both', expand=True)
        self.text2.insert(1.0,"   "+self.mass[0][i][2]+"\n")
        self.text2.insert(2.0,"   "+ self.mass[0][i][3]+"\n")
        self.text2.insert(3.0,self.mass[0][2][0])
        self.button = Button(root2,text="Зберегти як", width=20, bg='gray45')
        self.button.pack()
    def search(self,event):

        self.dat_now()
        self.text1.delete(1.0, END)

        key = self.text2.get(1.0,1.999)
        # Пошук ключового слова в БД
        text = Working_with_BD(self.choised_region(),self.dat_now()).search(key)

        self.canvas = []
        for i in range(text.__len__()):
            height =len(text[i][2])
            h = 10
            while  height > 50:
                h = h + 1
                height = height - 10
            height = len(text[i][3])
            h2 = 0
            while  height > 50:
                h2 = h2 + 1
                height = height - 10

            if text[i][4] == 'Новоград Волинський':
                tt = '{0}'.format('\t'*3)
            else:
                tt = '{0}'.format('\t'*4)

            Date = str(text[i][1])[8:10] + ':' + str(text[i][1])[10:12] + ' ' + str(text[i][1])[6:8] + '-' + str(
                text[i][1])[4:6] + '-' + str(text[i][1])[0:4]
            self.canvas.append(Canvas(width=510, height= 7*(h) + 3*h2 , bg='lightblue', ))
            self.canvas[i].create_text(10, 13, width=510, text=text[i][4] + tt + Date ,
                                       font="Calibry", justify=LEFT, fill='indigo', anchor="nw")
            self.canvas[i].create_text(10, 32, width=510, text="      "+text[i][2], font="Calibry", fill='red4',
                                       anchor="nw",justify=CENTER)
            self.canvas[i].create_text(10, h*5.3,width=510, text="     "+text[i][3], font="Calibry", fill='gray', anchor="nw")

            self.text1.window_create(CURRENT, window=self.canvas[i])


if __name__ == '__main__':
    root = Tk()
    root.geometry("555x680")
    root.title("Агрегатор новин житомирської області")
    app = Constructors()
    root.mainloop()
