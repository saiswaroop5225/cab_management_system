from tkinter import *
from tkinter import messagebox
import sqlite3

con=sqlite3.connect('database.db')
cur=con.cursor()



class Regpage(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x550+620+200")
        self.title("Registration Page")
        self.resizable(False,False)

        # frames........
        self.Top = Frame(self, height=130, bg="white")
        self.Top.pack(fill=X)
        self.Bottom = Frame(self, height=650, bg="#FA58F4")
        self.Bottom.pack(fill=X)

        # Heading... , Image....
        self.top_image = PhotoImage(file="iconmember.png")
        self.top_image_lbl = Label(self.Top, image=self.top_image, bg="white")
        self.top_image_lbl.place(x=120, y=10)
        self.heading = Label(self.Top, text="Regsitration Page !!", font="sans-serif 20 bold", fg="#8A0829",
                             bg="white")
        self.heading.place(x=280, y=60)

        #first name..............
        self.Fname=Label(self.Bottom,text=" Fname :",font="sans-serif",bg="#FA58F4")
        self.Fname.place(x=20,y=10)
        self.Fentry=Entry(self.Bottom,width=15,font="arial,8",bg="#F2F2F2")
        self.Fentry.place(x=120,y=13)
        self.Fentry.insert(0,"fname")

        # Last name..............
        self.Lname = Label(self.Bottom, text=" Lname :", font="sans-serif", bg="#FA58F4")
        self.Lname.place(x=320, y=10)
        self.Lentry = Entry(self.Bottom, width=15, font="arial,8,bold",bg="#F2F2F2")
        self.Lentry.place(x=420, y=13)
        self.Lentry.insert(0, "Lname")

        # Email..............
        self.Email = Label(self.Bottom, text=" Email :", font="sans-serif", bg="#FA58F4")
        self.Email.place(x=20, y=50)
        self.mail = Entry(self.Bottom, width=42, font="arial,8",bg="#F2F2F2")
        self.mail.place(x=120, y=53)
        self.mail.insert(0, "Please enter Email.........@gmail.com")

        # Mobile Number..............
        self.Number = Label(self.Bottom, text=" Mobile :", font="sans-serif", bg="#FA58F4")
        self.Number.place(x=20, y=95)
        self.Num = Entry(self.Bottom, width=42, font="arial,8",bg="#F2F2F2")
        self.Num.place(x=120, y=98)
        self.Num.insert(0, "Please enter mobile Number...+91987654321")

        # Password here..............
        self.Password = Label(self.Bottom, text=" Password :", font="sans-serif", bg="#FA58F4")
        self.Password.place(x=20, y=135)
        self.Pass = Entry(self.Bottom, width=42, font="arial,8",bg="#F2F2F2")
        self.Pass.place(x=120, y=138)
        self.Pass.insert(0, "Please enter password atleast 6 characters")

        # Address Here.................................
        self.Address=Label(self.Bottom,text=" Address :" ,font="sans-serif", bg="#FA58F4")
        self.Address.place(x=20, y=175)
        self.Add=Text(self.Bottom,width=58,height=7,bg="#F2F2F2",)
        self.Add.place(x=120,y=178)


        # Registration button ..................
        self.button=Button(self.Bottom,width=30,text="Sign Up",font="sans-serif 11 bold",fg="white",bg="#6E6E6E",command=self.addregister)
        self.button.place(x=220 , y=318)

    def addregister(self):
        firstname=self.Fentry.get()
        print(firstname)
        lastname=self.Lentry.get()
        print(lastname)
        email=self.mail.get()
        print(email)
        number=self.Num.get()
        print(number)
        password=self.Pass.get()
        print(password)
        address=self.Add.get(1.0,"end-1c")
        print(address)

        if(firstname!=""):
            pass
        else:
            messagebox.showerror("Error","please enter firstname",icon="warning")


        if(lastname!=""):
            pass
        else:
            messagebox.showerror("Error","please enter Lastname",icon="warning")

        if (email!=""):
            pass
        else:
            messagebox.showerror("Error","please enter email",icon="warning")

        if (number != ""):
            pass
        else:
            messagebox.showerror("Error", "please enter number", icon="warning")


        if (password!=""):
            pass
        else:
            messagebox.showerror("Error","please enter password",icon="warning")

        if (address!=""):
            pass
        else:
            messagebox.showerror("Error","please enter address",icon="warning")


        if(firstname and lastname and email and number and address !=""):
            try:
                query = "INSERT INTO 'Users'(first_name,last_name,email,number,password,address) VALUES(?,?,?,?,?,?)"
                cur.execute(query, (firstname,lastname,email,number,password,address))
                con.commit()
                messagebox.showerror("succesfull", "succesfully added you",icon="info")
            except:
                messagebox.showerror("Error", "please enter firstname", icon="warning")
        else:
            messagebox.showerror("Error","please enter all details",icon="warning")
