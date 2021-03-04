from tkinter import *
import Login_page
import datetime
import signup
import updatesignin
import about


date=datetime.datetime.now().date()

class Application(object):
    def __init__(self,master):
        self.master = master
        #frames........
        self.Top=Frame(master,height=150,bg="white")
        self.Top.pack(fill=X)
        self.Bottom=Frame(master,height=500,bg="#81F79F")
        self.Bottom.pack(fill=X)

        # Heading... , Image.... and Date.......
        self.top_image=PhotoImage(file="cab_mainpage_icon_6.png")
        self.top_image_lbl=Label(self.Top,image=self.top_image,bg="white")
        self.top_image_lbl.place(x=120,y=10)
        self.heading=Label(self.Top,text="Cab Booking at LPU !!",font="sans-serif 20 bold",fg="#8A0829",bg="white")
        self.heading.place(x=280,y=60)
        self.date=Label(self.Top,text="Today's Date: " + str(date),font="sans-serif 9",fg="black",bg="white")
        self.date.place(x=495,y=3)
        #My first button.....
        self.btn1icon=PhotoImage(file="user-female-circle (1).png")
        self.userbutton=Button(self.Bottom,text="  User Login page  ",font="arial 9 bold",command=self.openLogin_Page)
        self.userbutton.config(image=self.btn1icon,compound=LEFT)
        self.userbutton.place(x=270,y=10)

        # My second button.....
        self.btn2icon = PhotoImage(file="user.png")
        self.registerbutton = Button(self.Bottom, text=" Registration page", font="arial 9 bold",command=self.openregpage)
        self.registerbutton.config(image=self.btn2icon, compound=LEFT)
        self.registerbutton.place(x=270, y=80)

        # My Third button.....
        self.btn3icon = PhotoImage(file="edit-user-male.png")
        self.updatebutton = Button(self.Bottom, text="     Update Profile   ", font="arial 9 bold",command=self.openupdate)
        self.updatebutton.config(image=self.btn3icon, compound=LEFT)
        self.updatebutton.place(x=270, y=148)

        # My Fourth button.....
        self.btn4icon = PhotoImage(file="contract-job.png")
        self.Aboutbutton = Button(self.Bottom, text="    About this page  ", font="arial 9 bold",command=self.openabout)
        self.Aboutbutton.config(image=self.btn4icon, compound=LEFT)
        self.Aboutbutton.place(x=270, y=216)

    def openLogin_Page(self):
        login=Login_page.Loginpage()

    def openregpage(self):
        sign=signup.Regpage()

    def openupdate(self):
        update=updatesignin.Updatepage()

    def openabout(self):
        About=about.AboutUs()


def main():
    root=Tk()
    app = Application(root)
    root.title("Car Booking at LPU")
    root.geometry("650x550+350+100")
    root.iconbitmap("places_ico.ico")
    root.resizable(False,False)
    root.mainloop()
if __name__=='__main__':
    main()
