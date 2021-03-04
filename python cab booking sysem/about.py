from tkinter import *

class AboutUs(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+620+200")
        self.title("Login Page")
        self.resizable(False,False)

        # frames........
        self.Top = Frame(self, height=130, bg="white")
        self.Top.pack(fill=X)
        self.Bottom = Frame(self, height=650, bg="#585858")
        self.Bottom.pack(fill=X)

        # Heading... , Image.... and Date.......
        self.top_image = PhotoImage(file="cab_mainpage_icon_6.png")
        self.top_image_lbl = Label(self.Top, image=self.top_image, bg="white")
        self.top_image_lbl.place(x=120, y=10)
        self.heading = Label(self.Top, text="About Us !!", font="sans-serif 20 bold", fg="#8A0829",
                             bg="white")
        self.heading.place(x=280, y=60)

        #bottom............
        self.inf=Label(self.Bottom,text="Online Car Booking management System is developed to manage all cab \n"
                                        " hiring work online. It useful for car booking agency that are \n"
                                        "specialized in Hiring cabs to customers. Using this system many\n"
                                        " car-booking agency are moving ahead to become a pioneer in the\n"
                                        " vehicle rental industry by completely focusing on customers.\n"
                                        " Using this system it is very easy for customer to book a car\n"
                                        " online and car-booking agency can also track their booking online.\n"
                                        " So it is also very useful for car booking agency. It is an online \n"
                                        "system through which customers can view available cabs; register the\n"
                                        " cabs, view profile and book cabs. Mostly peoples use cab service for \n"
                                        "their daily transportations need. Car booking agency can also check which\n"
                                        " car is free for booking and which cars are on booking at present time.\n"
                                        " The objective and scope of my project Online Cab or car booking System\n"
                                        " is to record the details various activities of user. It will simplify\n"
                                        " the task and reduce the paper work. Using this car booking management\n"
                                        " system car owner can also become partner of car booking agency by giving \n"
                                        "their car for booking. Online Car rental management system is a web based\n"
                                        " application that allow users to book a car online  From this system car rental\n"
                                        " company can manage all car bookings and customer information. User can book cars\n"
                                        " and admin can confirm the booking and cancel the booking on the basis of availability\n"
                                        " of the cars and drivers.We have develop this system to produce a web-based system that\n"
                                        " allow customer to register and reserve cab online and for the company to effectively manage\n"
                                        " their Cab hiring business. Presently car booking agency do all work offline when a customer\n"
                                        " comes to them they take the booking order and call the car driver to check their availability\n"
                                        " with their car if they manage to find a car for booking they confirm the order otherwise\n"
                                        " they cancel the order as they have no car for the booking. This process waste a lot of time\n"
                                        " of customer and also of car booking agency and it also give bad name to the agency but with\n"
                                        " our system car agency can confirm the order within a minute by checking the availability of \n"
                                        "cars for booking. So this car booking system is helpful to ease customer’s task whenever they \n"
                                        "need to rent a cab or hire a cab.\n"
                                         "Thank you for visiting !!!!!!!!!!!"
                                        ,fg="white",font="sans-serif 10 bold"
                      , bg="#585858")
        self.inf.pack()




