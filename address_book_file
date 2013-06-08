from Tkinter import *
import os
import sys
"""
from tkintertable.Tables import TableCanvas
from tkintertable.TablesModels import TableModel
import Pmw

#https://code.google.com/p/tkintertable/wiki/Usage
tframe = Frame(master)
tframe.pack()
table = TableCanvas(tframe)
table.createTableFrame()

"""
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        #self.initUI()
        self.parent.title("Agenda Telefonica")
        self.pack(fill=BOTH, expand=1)
        # afisam fereastra in centru
        self.centerWindow()
        LNume = Label(self, text="Nume: ").grid(row=0)
        LEmail = Label(self, text="Email: ").grid(row=1)
        LTelefon = Label(self, text="Tel: ").grid(row=2)
        e1 = Entry(self)
        e2 = Entry(self)
        e3 = Entry(self)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        

        
        #buton de inchidere a aplicatiei
        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.grid(row=4)

        

    def centerWindow(self):
        w = 290
        h = 150
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
"""
    def initUI(self):
        self.parent.title("Agenda Telefonica")
        self.pack(fill=BOTH, expand=1)
"""
def main():
    root = Tk()
    #root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ =="__main__":
    main()


"""

table = Tktable.Table(top, rows = 5, cols = 5)
table.pack()
top = Tkinter.Tk()
#aici includem codul de afisat in fereastra
top.mainloop()
"""
