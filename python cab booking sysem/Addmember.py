from tkinter import *
from tkinter import messagebox
import sqlite3
con=sqlite3.connect('cabbooking.db')
cur=con.cursor()


class Add_member(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Book")
        self.resizable(False,False)
        #######################Frames#######################

        # Top Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)
        # Bottom Frame
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # heading, image
        self.top_image = PhotoImage(file='cab_mainpage_icon_6.png')
        top_image_lbl = Label(self.topFrame, image=self.top_image, bg='white')
        top_image_lbl.place(x=120, y=10)
        heading = Label(self.topFrame, text='  Add Members ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)

        ###########################################Entries and Labels########################3

        # name
        self.lbl_name = Label(self.bottomFrame, text='Name :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottomFrame, width=30, bd=1)
        self.ent_name.insert(0, 'Please Enter your Name')
        self.ent_name.place(x=150, y=45)
        # phone number of passenger
        self.lbl_phone = Label(self.bottomFrame, text='Phone :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=80)
        self.ent_phone = Entry(self.bottomFrame, width=30, bd=1)
        self.ent_phone.insert(0, ' Please Enter mobile number')
        self.ent_phone.place(x=150, y=85)


        # Button
        button = Button(self.bottomFrame, text='Add member', command=self.addCar)
        button.place(x=270, y=130)

    def addCar(self):
        name = self.ent_name.get()
        phone = self.ent_phone.get()


        if (name and phone !=""):
            try:
                query = "INSERT INTO 'Users' (User_name,User_phone) VALUES(?,?)"
                cur.execute(query,(name,phone))
                con.commit()
                messagebox.showinfo("Success", "Successfully added to database", icon='info')

            except:
                messagebox.showerror("Error", "Cant add to database", icon='warning')
        else:
            messagebox.showerror("Error", "Fields cant be empty", icon='warning')