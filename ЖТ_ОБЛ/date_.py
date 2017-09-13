import tkinter.ttk as ttk
import tkinter as tk
from datetime import datetime, timedelta

class sel_date(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.d = 0
        self.m = 0
        self.y = 0
        self.active = True

        self.line = ttk.Label(self, width=10, relief='groove')
        self.show()
        self.line.bind('<Button-1>', lambda event: self.up_value(event, 1))
        self.line.bind('<Button-3>', lambda event: self.up_value(event, -1))
        self.line.bind('<Shift-Button-1>', lambda event: self.up_value(event, 10))
        self.line.bind('<Shift-Button-3>', lambda event: self.up_value(event, -10))
        self.line.pack(fill='y')

    def up_value(self, event, bt):
        if not self.active:
            return
        if int(event.x) < 30:
            self.y += bt
        elif int(event.x) < 48:
            self.m = 12 if self.m + bt < 1 else 1 \
                if self.m + bt > 12 else self.m + bt

            if self.m == 2 and self.d > 27:
                if (self.y % 400 == 0) or ((self.y % 100 != 0) and (self.y % 4 == 0)):
                    self.d = 29
                else:
                    self.d = 28
            else:
                if self.m in [4, 6, 9, 11] and self.d > 30:
                    self.d = 30
        else:
            max_d = 31
            if self.m == '2':
                if (self.y % 400 == 0) or ((self.y % 100 != 0) and (self.y % 4 == 0)):
                    max_d = 29
                else:
                    max_d = 28
            else:
                if self.d in ['4', '6', '9', '11']:
                    max_d = 30
            self.d = max_d if self.d + bt < 1 else 1 \
                if self.d + bt > max_d else self.d + bt
        self.show(False)

    def show(self, f=True):
        if f:
            self.d = datetime.today().day
            self.m = datetime.today().month
            self.y = datetime.today().year
        self.line['text'] = '{:0>4}.{:0>2}.{:0>2}'.format(self.y, self.m, self.d)

    def state_(self, zn=True):
        self.active = zn
        self.line['foreground'] = 'black' if zn else 'white'

    def get_dt(self, f=False):
        return datetime(self.y, self.m, self.d, 23, 59, 59, 0) if f else datetime(self.y, self.m, self.d, 0, 0, 0, 0)

    def get_date(self, iso_=False):
        return datetime(self.y, self.m, self.d).date().isoformat() if iso_ \
            else datetime(self.y, self.m, self.d).date()

    def set_dt(self, zn):
        if type(zn) is int:
            self.d = int(str(zn)[6:])
            self.m = int(str(zn)[4:6])
            self.y = int(str(zn)[:4])
        else:
            self.d = zn.day
            self.m = zn.month
            self.y = zn.year
        self.show(f=False)
