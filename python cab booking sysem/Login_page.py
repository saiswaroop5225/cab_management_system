from tkinter import *
import sqlite3
import window
from tkinter import messagebox



con=sqlite3.connect('database.db')
cur=con.cursor()


class Loginpage(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x450+620+200")
        self.title("Login Page")
        self.resizable(False,False)

        # frames........
        self.Top = Frame(self, height=150, bg="white")
        self.Top.pack(fill=X)
        self.Bottom = Frame(self, height=400, bg="#8181F7")
        self.Bottom.pack(fill=X)

        # Heading... , Image....
        self.top_image = PhotoImage(file="log.png")
        self.top_image_lbl = Label(self.Top, image=self.top_image, bg="white")
        self.top_image_lbl.place(x=120, y=10)
        self.heading = Label(self.Top, text="Login Page !!", font="sans-serif 20 bold", fg="#8A0829",
                             bg="white")
        self.heading.place(x=280, y=60)


        #user name..............
        self.Username=Label(self.Bottom,text="Username :",font="sans-serif 20 bold ",bg="#8181F7",fg="#FAFAFA")
        self.Username.place(x=100,y=40)
        self.Uname=Entry(self.Bottom,width=25,font="sans-serif,15")
        self.Uname.insert(0,"please enter username")
        self.Uname.place(x=270,y=46)

        #password.................
        self.Password=Label(self.Bottom,text="Password :",font="sans-serif 20 bold",bg="#8181F7",fg="#FAFAFA")
        self.Password.place(x=100,y=100)
        self.Pname = Entry(self.Bottom, width=25, font="sans-serif,15")
        self.Pname.insert(0, "please enter Password")
        self.Pname.place(x=270, y=100)
        self.Pname.config(show="*")


        #Sign In button............
        self.button1=Button(self.Bottom,text="Sign In",width=25,font="sans-serif 11",bg="#6E6E6E",
                            fg="white",command=self.openwindow)
        self.button1.place(x=220,y=170)

        ##########################DATA BASE############################################
        user_email=cur.execute("SELECT email FROM Users").fetchall()
        print(user_email)
        user_password=cur.execute("SELECT password FROM Users").fetchall()
        print(user_password)

    def openwindow(self):
        ement=self.Uname.get()
        passw=self.Pname.get()
        print(ement)
        print(passw)
        if (ement and passw !=""):
            messagebox.showinfo("SUCCESS","successfully Logged in",icon="info")
            windo = window.Main()
        else:
            messagebox.showerror("ERROR","please fill all details",icon="warning")























   


















