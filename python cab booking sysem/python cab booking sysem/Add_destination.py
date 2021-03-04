from tkinter import *
from tkinter import messagebox
import sqlite3

con=sqlite3.connect('cabbooking.db')
cur=con.cursor()


class Add_Destination(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Route")
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
        heading = Label(self.topFrame, text='  Add Route ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)

        ###########################################Entries and Labels########################3

        # name
        self.lbl_start = Label(self.bottomFrame, text='Starting Point :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_start.place(x=40, y=40)
        self.ent_start = Entry(self.bottomFrame, width=30, bd=1)
        self.ent_start.insert(0, 'Please Enter your strating point')
        self.ent_start.place(x=250, y=45)
        # phone number of passenger
        self.lbl_dest = Label(self.bottomFrame, text='Destination Point:', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_dest.place(x=40, y=80)
        self.ent_dest = Entry(self.bottomFrame, width=30, bd=1)
        self.ent_dest.insert(0, ' Please Enter destination')
        self.ent_dest.place(x=250, y=85)
        #phone number........
        self.lbl_phone = Label(self.bottomFrame, text='phone Number:', font='asrial 15 bold', fg='white',
                              bg='#fcc324')
        self.lbl_phone.place(x=40, y=125)
        self.ent_phone = Entry(self.bottomFrame, width=30, bd=1)
        self.ent_phone.insert(0, ' Please Enter Phone Number')
        self.ent_phone.place(x=250, y=125)


        # Button
        button = Button(self.bottomFrame, text='Add Route', command=self.addCar)
        button.place(x=270, y=170)

    def addCar(self):
        start = self.ent_start.get()
        dest = self.ent_dest.get()
        phone=self.ent_phone.get()


        if (start and dest and phone !=""):
            try:
                query = "INSERT INTO 'destination' (starting,destination,phone) VALUES(?,?,?)"
                cur.execute(query,(start,dest,phone))
                con.commit()
                messagebox.showinfo("Success", "Successfully booked", icon='info')

            except:
                messagebox.showerror("Error", "something went wrong", icon='warning')
        else:
            messagebox.showerror("Error", "Fields cant be empty", icon='warning')