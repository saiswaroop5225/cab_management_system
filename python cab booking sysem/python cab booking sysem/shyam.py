from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import couriermanagementsystem,Addmember,Add_destination


con=sqlite3.connect('couriermanagementsystem.db')
cur=con.cursor()

class Main(object):
    def __init__(self,master):
        self.master = master

        def displayStatistics(evt):
            count_cars = cur.execute("SELECT count(courier_id) FROM courier_booking").fetchall()
            count_members = cur.execute("SELECT count(User_id) FROM Users").fetchall()
            booked_cars = cur.execute("SELECT count(courier_status) FROM courier_booking WHERE courier_status=1").fetchall()
            print(count_cars)
            self.lbl_car_count.config(text='Total :' + str(count_cars[0][0]) + ' courier available')
            self.lbl_member_count.config(text="Total users : " + str(count_members[0][0]))
            self.lbl_taken_count.config(text="Booked courier:" + str(booked_cars[0][0]))
            displaycars(self)

        def displaycars(self):
            cars = cur.execute("SELECT * FROM Cab_booking").fetchall()
            count = 0
            self.list_cars.delete(0, END)
            for car in cars:
                print(car)
                self.list_cars.insert(count, str(car[0]) + "-" + car[1] +"--"+car[2]+"--"+str(car[5]))
                count += 1

            def carInfo(evt):
                value=str(self.list_cars.get(self.list_cars.curselection()))
                id=value.split('-')[0]
                courier =cur.execute("SELECT * FROM courier_booking WHERE courier_id=?",(id,))
                courier_info=courier.fetchall()
                print(car_info)
                self.list_details.delete(0,'end')
                self.list_details.insert(0,"courier Name : "+courier_info[0][1])
                self.list_details.insert(1,"courier type : "+courier_info[0][2])
                self.list_details.insert(2,"Model : "+courier_info[0][3])
                self.list_details.insert(3,"courier_status : "+str(courier_info[0][4]))
                if car_info[0][4] == 0:
                    self.list_details.insert(4,"Status : Avaiable")
                else:
                    self.list_details.insert(4,"Status : not Avaiable")

            def doubleClick(evt):
                global Booked_id
                value=str(self.list_courier.get(self.list_cars.curselection()))
                print(value)
                Booked_id = value.split('-')[0]
                Book_car = BookedCar()



            self.list_cars.bind('<<ListboxSelect>>', carInfo)
            self.tabs.bind('<<NotebookTabChanged>>', displayStatistics)
            self.list_cars.bind('<Double-Button-1>', doubleClick)




        #frames
        Mainframe=Frame(self.master)
        Mainframe.pack()
        #TOP FRAME..........................
        Topframe=Frame(Mainframe,width=1350,height=70,bg="#f8f8f8",padx=20,relief=SUNKEN,borderwidth=2)
        Topframe.pack(side=TOP,fill=X)
        #CENTER frame............................
        centerframe=Frame(Mainframe,width=1350,height=680,relief=RIDGE,bg="#e0f0f0")
        centerframe.pack(side=TOP)
        #central left frame.............
        Cleftframe=Frame(centerframe,width=900,height=700,relief=SUNKEN,bg="#e0f0f0",borderwidth=2)
        Cleftframe.pack(side=LEFT)
        #center right frame............
        Crightframe=Frame(centerframe,width=450,height=700,bg="#e0f0f0",relief=SUNKEN,borderwidth=2)
        Crightframe.pack()

        #search box...........
        search_bar = LabelFrame(Crightframe,width=440,height=70,text="Search Box",bg="#9bc9ff")
        search_bar.pack(fill=BOTH)
        self.lbl_search=Label(search_bar,text="Search",font="arial 12 bold",bg='#9bc9ff',fg='white')
        self.lbl_search.grid(row=0,column=0,padx=20,pady=10)
        self.lbl_entry=Entry(search_bar,width=30,border=3)
        self.lbl_entry.grid(row=0,column=1,columnspan=5,padx=10)
        self.bnt_search=Button(search_bar,text="search",font="sans-serif 12 bold",bg="grey",fg="white",command=self.searchcars)
        self.bnt_search.grid(row=0,column=7,pady=15,padx=10)

        #list box
        list_bar=LabelFrame(Crightframe,width=440,height=175,text="List box",bg="#F6CEE3")
        list_bar.pack(fill=BOTH)
        self.lbl_list=Label(list_bar,text="Sort By:-",font="sans-serif 12 bold",bg="#F6CEE3")
        self.lbl_list.grid(row=0,column=2)

        #radio buttons.......
        self.listchoice=IntVar()
        self.Radiobut1=Radiobutton(list_bar,text="All places",var=self.listchoice,value=1,bg="#F6CEE3")
        self.Radiobut2 = Radiobutton(list_bar, text="Cars Available", var=self.listchoice, value=2, bg="#F6CEE3")
        self.Radiobut3 = Radiobutton(list_bar, text="Booked cars", var=self.listchoice, value=3, bg="#F6CEE3")
        self.Radiobut1.grid(row=1,column=0)
        self.Radiobut2.grid(row=1,column=1)
        self.Radiobut3.grid(row=1,column=2)
        #button for list box which dispalys above radio details by clicking it.....
        self.btn_list=Button(list_bar,text="Click Me!",bg="#D8D8D8",font="sans-serif 12",command=self.listCars)
        self.btn_list.grid(row=1,column=3,pady=18,padx=35)


        #Book car.........
        self.bookcar=PhotoImage(file="Sportscar-car-icon.png")
        self.bookbutton=Button(Topframe,image=self.bookcar,text="BookCar",font="arial 11 bold",compound=LEFT,width=170,command=self.openBookcar)
        self.bookbutton.pack(side=LEFT,padx=10)
        # add destination................
        self.icondes = PhotoImage(file='adddes.png',height=30)
        self.Destinationbutton = Button(Topframe, image=self.icondes, text="Add Destination", font="arial 11 bold", compound=LEFT,width=170,height=45.1,command=self.opendestination)
        self.Destinationbutton.pack(side=LEFT,padx=1)
        # add Members to travell................

        self.iconMem = PhotoImage(file='iconmember.png')
        self.Addmembutton = Button(Topframe, image=self.iconMem, text="Add Member", font="arial 11 bold",
                                        compound=LEFT, width=170, height=43,command=self.openmem)
        self.Addmembutton.pack(side=LEFT, padx=6)
        #title and image for various tabs and create a good looking app
        image_bar=Frame(Crightframe,width=440,height=350)
        image_bar.pack(fill=BOTH)
        self.title_right=Label(image_bar,text="welcome to car booking management",font="sans-serif 15   bold")
        self.title_right.grid(row=0)
        self.image_cab=PhotoImage(file="car-loan.png")
        self.image_lbl=Label(image_bar,image=self.image_cab)
        self.image_lbl.grid(row=1)

        #########################TOOL BAR#####################################################################

        #########################TABS>>>>>>>......##################################
        self.tabs = ttk.Notebook(Cleftframe, width=900, height=660)
        self.tabs.pack()
        self.tab1_icon = PhotoImage(file='user.png')
        self.tab2_icon = PhotoImage(file='contract-job.png')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text='self.tabs.add(self.tab1, text='self.tabs.add(self.tab1, text='courier Management', image=self.tab1_icon, compound= Management', image=self.tab1_icon, compound=LEFT) Management', image=self.tab1_icon, compound=LEFT)
        self.tabs.add(self.tab2, text='Statistics of Management', image=self.tab2_icon, compound=LEFT)

        # list books
        self.list_cars = Listbox(self.tab1, width=40, height=30, bd=5, font='times 12 bold')
        self.sb = Scrollbar(self.tab1, orient=VERTICAL)
        self.list_cars.grid(row=0, column=0, padx=(10, 0), pady=10, sticky=N)
        self.sb.config(command=self.list_cars.yview)
        self.list_cars  .config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=0, sticky=N + S + E)

        # list details
        self.list_details = Listbox(self.tab1, width=80, height=30, bd=5, font='times 12 bold')
        self.list_details.grid(row=0, column=1, padx=(10, 0), pady=10, sticky=N)
        ##########################tab2####################################
        # statistics
        self.lbl_car_count = Label(self.tab2, text="adfafs", pady=20, font='verdana 14 bold')
        self.lbl_car_count.grid(row=0)
        self.lbl_member_count = Label(self.tab2, text="asdfadsf", pady=20, font='verdana 14 bold')
        self.lbl_member_count.grid(row=1, sticky=W)
        self.lbl_taken_count = Label(self.tab2, text="asdfdafd", pady=20, font='verdana 14 bold')
        self.lbl_taken_count.grid(row=2, sticky=W)
        displaycars(self)
        displayStatistics(self)

    def opendestination(self):
        des=Add_destination.Add_Destination()

    def openBookcar(self):
        bookcar=Bookcar.Book_car()

    def openmem(self):
        open=Addmember.Add_member()

    def searchcars(self):
        value = self.lbl_entry.get()
        search = cur.execute("SELECT * FROM Cab_booking WHERE car_type LIKE ?", ('%' + value + '%',)).fetchall()
        print(search)
        self.list_cars.delete(0, END)
        count = 0
        for car in search:
            self.list_cars.insert(count, str(car[0]) + "-" + car[1]+ "--" +car[2])
            count += 1
    def listCars(self):
        value = self.listchoice.get()
        if value == 1:
            allcars= cur.execute("SELECT * FROM Cab_booking").fetchall()
            self.list_cars.delete(0,END)

            count=0
            for car in allcars:
                self.list_cars.insert(count,str(car[0]) + "-"+car[1] + "--" +car[2])
                count +=1

        elif value == 2:
            car_in_parking= cur.execute("SELECT * FROM Cab_booking WHERE car_status =?",(0,)).fetchall()
            self.list_cars.delete(0, END)

            count = 0
            for car in car_in_parking:
                self.list_cars.insert(count, str(car[0]) + "-" + car[1] + "--" +car[2])
                count += 1
        else:
            taken_cars= cur.execute("SELECT * FROM Cab_booking WHERE car_status =?",(1,)).fetchall()
            self.list_cars.delete(0, END)

            count = 0
            for car in taken_cars:
                self.list_cars.insert(count, str(car[0]) + "-" + car[1] + "--" +car[2])

                count += 1


class BookedCar(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+500+250")
        self.title("Lend Car")
        self.iconbitmap("places_ico.ico")
        self.resizable(False,False)
        #####class starts from here.......................
        global Booked_id
        self.car_id = int(Booked_id)
        query = "SELECT * FROM Cab_booking"
        cars = cur.execute(query).fetchall()
        car_list = []
        for car in cars:
            car_list.append(str(car[0]) + "-" + car[1])

        query2 = "SELECT * FROM Users"
        members = cur.execute(query2).fetchall()
        member_list = []
        for member in members:
            member_list.append(str(member[0]) + "-" + member[1])

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
        self.car_type = StringVar()
        self.lbl_start = Label(self.bottomFrame, text='Car Type :', font='arial 15 bold', fg='white',
                               bg='#fcc324')
        self.lbl_start.place(x=40, y=40)
        self.combo_name = ttk.Combobox(self.bottomFrame, textvariable=self.car_type)
        self.combo_name['values'] = car_list
        self.combo_name.current(self.car_id - 1)
        self.combo_name.place(x=250, y=45)

        # phone number of passenger
        self.User_number = StringVar()
        self.lbl_member = Label(self.bottomFrame, text='User name:', font='arial 15 bold', fg='white',
                              bg='#fcc324')
        self.lbl_member.place(x=40, y=80)
        self.combo_member = ttk.Combobox(self.bottomFrame, textvariable=self.User_number)
        self.combo_member['values'] = member_list
        self.combo_member.place(x=250, y=85)




        # Button
        button = Button(self.bottomFrame, text='Book Car',command=self.LendCar)
        button.place(x=280, y=170)
    def LendCar(self):
        car_name = self.car_type.get()
        User_name = self.User_number.get()


        if (car_name and User_name  != ""):
            try:
                query = "INSERT INTO 'booked' (car_booked_id,user_booked_id) VALUES(?,?)"
                cur.execute(query, (car_name, User_name))
                con.commit()
                messagebox.showinfo("Success", "Successfully booked!", icon='info')
                cur.execute("UPDATE Cab_booking SET car_status =? WHERE car_id=?", (1, self.car_id))
                con.commit()

            except:
                messagebox.showerror("Succes", "Booked the car", icon='info')

        else:
            messagebox.showerror("Error", "Fields cant be empty", icon='warning')







def main():
    root = Tk()
    app = Main(root)
    root.title("Car Booking in LPU")
    root.geometry("1350x750+110+20")
    root.iconbitmap("places_ico.ico")
    root.resizable(False,False)
    root.mainloop()

if __name__=="__main__":
    main()

