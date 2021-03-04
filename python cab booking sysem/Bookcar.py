from tkinter import *
from tkinter import messagebox
import sqlite3
con=sqlite3.connect('cabbooking.db')
cur=con.cursor()


class Book_car(Toplevel):
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
        heading = Label(self.topFrame, text='  Add your trip. ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)

        ###########################################Entries and Labels########################3

        # name
        self.lbl_name = Label(self.bottomFrame, text='Name :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottomFrame, width=30, bd=1)
        self.ent_name.insert(0, 'Please Enter Car Name')
        self.ent_name.place(x=150, y=45)
        # Type of car user want
        self.lbl_Type = Label(self.bottomFrame, text='Type :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_Type.place(x=40, y=80)
        self.ent_Type = Entry(self.bottomFrame, width=30, bd=1)
        self.ent_Type.insert(0, ' Please Enter Car Type')
        self.ent_Type.place(x=150, y=85)
        # Type of model user want
        self.lbl_Model = Label(self.bottomFrame, text='Model :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_Model.place(x=40, y=120)
        self.ent_Model= Entry(self.bottomFrame, width=30, bd=1)
        self.ent_Model.insert(0, 'Please Enter Car Model ')
        self.ent_Model.place(x=150, y=125)

        # Button
        button = Button(self.bottomFrame, text='Add Car', command=self.addCar)
        button.place(x=270, y=200)

    def addCar(self):
        name = self.ent_name.get()
        type = self.ent_Type.get()
        model = self.ent_Model.get()

        if (name and type and model !=""):
            try:
                query = "INSERT INTO 'Cab_booking' (car_name,car_type,car_model) VALUES(?,?,?)"
                cur.execute(query,(name,type,model))
                con.commit()
                messagebox.showinfo("Success", "Successfully added to database", icon='info')

            except:
                messagebox.showerror("Error", "Cant add to database", icon='warning')
        else:
            messagebox.showerror("Error", "Fields cant be empty", icon='warning')