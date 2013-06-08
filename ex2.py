from Tkinter import *
import os
import tkFileDialog
import pickle
import sys
import contact


def add_contact():
    address_book_file= tkFileDialog.askopenfilename(mode="rw")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not is_file_empty:
        list_contacts=pickle.load(address_book_file)
    else:
        list_contacts=[]
    try:
        contact=getContact()
        address_book_file=open("address_book_file","w")
        list_contacts.append(contact)
        pickle.dump(list_contacts,address_book_file)
        print "Contact added"
    except KeyboardInterrupt:
        print "Contact not added"
    except EOFError:
        print "Contact not added"
    finally:
        address_book_file.close()

def getContact():
    try:
        contactNume = e1.get()
        contactEmail = e2.get()
        contactTel = e3.get()
        contact = Contact(contactNume, contactEmail, contactTel)
        return contact
    except EOFError as e:
        raise e
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
        addContactButton = Button(self, text="AddContact", command=self.askopenfile)
        addContactButton.grid(row=5, column=1)

    def askopenfile(self):
        return tkFileDialog.askopenfile(mode="r")

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
    #root.distroy()

if __name__ =="__main__":
    main()

"""
def add_contact():
    address_book_file=open("address_book_file","r")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not is_file_empty:
        list_contacts=pickle.load(address_book_file)
    else:
        list_contacts=[]
    try:
        contact=get_contact_info_from_user()
        address_book_file=open("address_book_file","w")
        list_contacts.append(contact)
        pickle.dump(list_contacts,address_book_file)
        print "Contact added"
    except KeyboardInterrupt:
        print "Contact not added"
    except EOFError:
        print "Contact not added"
    finally:
        address_book_file.close()

"""
