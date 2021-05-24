import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector
from intro import intro
from function import refresh, add_citizen, update_citizen, delete_citizen, search
from function2 import add_enterprise, update_enterprise, delete_enterprise, search1, refresh1
#define window

class windowclass():
    def __init__(self, window):
        self.window = window
        self.frame = Frame(window)
        self.frame.pack()

        #define tab:
        self.tabControl = ttk.Notebook(window)
        self.tab0 = Frame(self.tabControl)
        self.tab1 = Frame(self.tabControl)
        self.tab2 = Frame(self.tabControl)
        self.tab3 = Frame(self.tabControl)

        self.tabControl.add(self.tab0, text="Introduce")
        self.tabControl.add(self.tab1, text="Citizen")
        self.tabControl.add(self.tab2, text="Enterprise")
        self.tabControl.add(self.tab3, text="Support")
        self.tabControl.pack(expand=1, fill=BOTH)

        #define tab0
        self.bg0 = Image.open("bg.jpeg")
        self.resize0 = self.bg0.resize((1100,650), Image.ANTIALIAS)
        self.newbg0 = ImageTk.PhotoImage(self.resize0)
        self.label0 = Label(self.tab0, image=self.newbg0)
        self.label0.place(x=0,y=0)
        self.welcome = Label(self.tab0, text="Welcome", font=("times new roman", 60, "bold"), bg= "white")
        self.welcome.place(x=400, y=300)
        self.button = Button(self.tab0, text="Read",font=("times new roman", 15, "bold"), fg='black',bg='#0080FF', bd=5, relief=GROOVE, command=lambda :self.read())
        self.button.pack(side=BOTTOM)
        self.button0 = Button(self.tab0, text="Exit",font=("times new roman", 15, "bold"), fg='black',bg='#0080FF', bd=5, relief=GROOVE, command=lambda :self.exit())
        self.button0.pack(side=BOTTOM)

        #define tab1

        self.label1 = Label(self.tab1, image=self.newbg0)
        self.label1.place(x=0, y=0)
        #define tab2
        self.label2 = Label(self.tab2, image=self.newbg0)
        self.label2.place(x=0,y=0)

        #design tab1
        self.frame1 = Frame(self.tab1, bg="#B0C4DE", relief=FLAT)
        self.frame1.place(x=5, y=5, width=1090, height=300)

        self.label = Label(self.frame1, text="Citizen information", font=("times new roman", 15, "bold"), bg='black',fg="white")
        self.label.place(x=0, y=0, width=1090)

        self.firstname = Label(self.frame1, text="First name", font=("times new roman", 12, "bold"), fg="black",bg="#B0C4D3")
        self.firstname.place(x=20, y=30)
        self.fentry = Entry(self.frame1, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.fentry.place(x=20, y=60, width=250)

        self.lastname = Label(self.frame1, text="Last name", font=("times new roman", 12, "bold"), fg="black",bg="#B0C4D3")
        self.lastname.place(x=320, y=30)
        self.lentry = Entry(self.frame1, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.lentry.place(x=320, y=60, width=250)

        self.yob = Label(self.frame1, text="Year of birth", font=("times new roman", 12, "bold"), fg="black",bg="#B0C4D3")
        self.yob.place(x=600, y=30)

        self.year_choice = ttk.Spinbox(self.frame1, from_=1950, to=2021, font=("times new roman", 12, "bold"))
        self.year_choice.place(x=600, y=60, width=120)
        self.year_choice.set("  -Select year-  ")

        self.cccd = Label(self.frame1, text="Citizen identification", font=("times new roman", 12, "bold"), fg="black",bg="#B0C4D3")
        self.cccd.place(x=20, y=120)
        self.cccd_entry = Entry(self.frame1, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.cccd_entry.place(x=20, y=150, width=250)

        self.where = Label(self.frame1, text="Home town", font=("times new roman", 12, "bold"), fg="black",bg="#B0C4D3")
        self.where.place(x=320, y=120)
        self.where_entry = Entry(self.frame1, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.where_entry.place(x=320, y=150, width=250)

        self.gender = Label(self.frame1, text="Gender", font=("times new roman", 12, "bold"), fg="black", bg="#B0C4D3")
        self.gender.place(x=600, y=120)
        a = ['Male', 'Female']
        self.gender_entry = ttk.Combobox(self.frame1, values=a, font=("times new roman", 12, "bold"))
        self.gender_entry.place(x=600, y=150, width=120)
        self.gender_entry.config(state="readonly")

        self.folk = Label(self.frame1, text="Folk", font=("times new roman", 12, "bold"), fg="black", bg="#B0C4D3")
        self.folk.place(x=20, y=210)
        self.folk_entry = Entry(self.frame1, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.folk_entry.place(x=20, y=240, width=120)

        self.contact = Label(self.frame1, text="Contact phone", font=("times new roman", 12, "bold"), fg="black",bg="#B0C4D3")
        self.contact.place(x=320, y=210)
        self.contact_entry = Entry(self.frame1, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.contact_entry.place(x=320, y=240, width=250)

        self.marital = Label(self.frame1, text="Marital status", font=("times new roman", 12, "bold"), fg="black",bg="#B0C4D3")
        self.marital.place(x=600, y=210)
        b = ['Single', 'Married', 'Divorced']
        self.marital_choice = ttk.Combobox(self.frame1, values=b, font=("times new roman", 12, "bold"))
        self.marital_choice.place(x=600, y=240, width=120)
        self.marital_choice.config(state="readonly")

        self.addbutton = Button(self.frame1, text="Add", font=("times new roman", 15, "bold"), fg='black', bg='#0080FF',bd=5, relief=GROOVE, command=lambda :add_citizen(self))
        self.addbutton.place(x=800, y=40, width=200)

        self.updatebutton = Button(self.frame1, text="Update", font=("times new roman", 15, "bold"), fg='black',bg='#0080FF', bd=5, relief=GROOVE, command=lambda :update_citizen(self))
        self.updatebutton.place(x=800, y=110, width=200)

        self.deletebutton = Button(self.frame1, text="Delete", font=("times new roman", 15, "bold"), fg='black',bg='#0080FF', bd=5, relief=GROOVE, command=lambda :delete_citizen(self))
        self.deletebutton.place(x=800, y=180, width=200)

        self.refreshbutton = Button(self.frame1, text="Refresh", font=("times new roman", 15, "bold"), fg='black',bg='#0080FF', bd=5, relief=GROOVE, command=lambda :refresh(self))
        self.refreshbutton.place(x=800, y=250, width=200)

        self.frame2 = Frame(self.tab1, relief=FLAT, bg="#B0C4DE")
        self.frame2.place(x=5, y=310,width=1090, height=300)

        self.frame3 = Frame(self.frame2, relief=FLAT, bg="white")
        self.frame3.place(x=5, y=5, width=1080, height=55)

        self.frame4 = Frame(self.frame2, relief=FLAT, bg="white")
        self.frame4.place(x=5, y=60,width=1080, height=240)

        self.searchby = Label(self.frame3, text="Search: ", font=("Times new roman", 12, "bold"), fg="black",bg="white")
        self.searchby.place(x=100, y=10)

        c = ["Lastname", "CI", "Contact"]
        self.searchcombo = ttk.Combobox(self.frame3, values=c, font=("times new roman", 12, "bold"))
        self.searchcombo.place(x=180, y=10, width=200)
        self.searchcombo.set("Select option")
        self.searchcombo.config(state="readonly")

        self.search_entry = Entry(self.frame3, font=("times new roman", 12, "bold"))
        self.search_entry.place(x=400, y=10, width=250)

        self.searchbutton = Button(self.frame3, text="Search", font=("times new roman", 12, "bold"), fg='black',bg='#0080FF', bd=5, relief=GROOVE, command=lambda : search(self))
        self.searchbutton.place(x=700, y=10, width=100)

        self.showbutton = Button(self.frame3, text="Show", font=("times new roman", 12, "bold"), fg='black',bg='#0080FF', bd=5, relief=GROOVE, command=lambda :self.showall())
        self.showbutton.place(x=900, y=10, width=100)

        self.tree_scroll = Scrollbar(self.frame4)
        self.treeview = ttk.Treeview(self.frame4, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings",yscrollcommand=self.tree_scroll.set)
        self.tree_scroll.pack(side=RIGHT, fill= Y)
        self.tree_scroll.config(command=self.treeview.yview)

        self.treeview.heading(1, text="First name")
        self.treeview.heading(2, text="Last name")
        self.treeview.heading(3, text="Year of birth")
        self.treeview.heading(4, text="Citizen Identification")
        self.treeview.heading(5, text="Home town")
        self.treeview.heading(6, text="Gender")
        self.treeview.heading(7, text="Folk")
        self.treeview.heading(8, text="Contact phone")
        self.treeview.heading(9, text="Marital status")

        self.treeview.column(1, width=100)
        self.treeview.column(2, width=100)
        self.treeview.column(3, width=100)
        self.treeview.column(4, width=100)
        self.treeview.column(5, width=100)
        self.treeview.column(6, width=70)
        self.treeview.column(7, width=70)
        self.treeview.column(8, width=100)
        self.treeview.column(9, width=100)

        self.treeview.place(x=5, y=0, width=1055)
        self.show()

        #design tab2
        self.frame21 = Frame(self.tab2, bg="#B0C4DE", relief=FLAT)
        self.frame21.place(x=5, y=5, width=1090, height=250)

        self.label21 = Label(self.frame21, text="Enterprise information", font=("times new roman", 15, "bold"), bg='black',fg="white")
        self.label21.place(x=0, y=0, width=1090)

        self.name = Label(self.frame21, text="Company's name", font=("times new roman", 12, "bold"), fg="black",bg="#B0C4D3")
        self.name.place(x=20, y=30)
        self.name_entry = Entry(self.frame21, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.name_entry.place(x=20, y=60, width=250)

        self.code = Label(self.frame21, text="Business code", font=("times new roman", 12, "bold"), fg="black",bg="#B0C4D3")
        self.code.place(x=400, y=30)
        self.code_entry = Entry(self.frame21, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.code_entry.place(x=400, y=60, width=250)

        self.year = Label(self.frame21, text="Founded year", font=("times new roman", 12, "bold"), fg="black",bg="#B0C4D3")
        self.year.place(x=800, y=30)
        self.year_entry = Entry(self.frame21, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.year_entry.place(x=800, y=60, width=250)

        self.type = Label(self.frame21, text="Business type", font=("times new roman", 12, "bold"), fg="black",bg="#B0C4D3")
        self.type.place(x=20, y=100)
        self.type_entry = Entry(self.frame21, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.type_entry.place(x=20, y=140, width=250)

        self.address = Label(self.frame21, text="Address", font=("times new roman", 12, "bold"), fg="black",bg="#B0C4D3")
        self.address.place(x=400, y=100)
        self.address_entry = Entry(self.frame21, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.address_entry.place(x=400, y=140, width=250)

        self.phone = Label(self.frame21, text="Contact", font=("times new roman", 12, "bold"), fg="black",bg="#B0C4D3")
        self.phone.place(x=800, y=100)
        self.phone_entry = Entry(self.frame21, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.phone_entry.place(x=800, y=140, width=250)

        self.addbutton1 = Button(self.frame21, text="Add", font=("times new roman", 15, "bold"), fg='black',bd=5, relief=GROOVE, command = lambda :add_enterprise(self))
        self.addbutton1.place(x=20, y=190, width=200)

        self.updatebutton1 = Button(self.frame21, text="Update", font=("times new roman", 15, "bold"), fg='black', bd=5, relief=GROOVE, command = lambda :update_enterprise(self))
        self.updatebutton1.place(x=300, y=190, width=200)

        self.deletebutton1 = Button(self.frame21, text="Delete", font=("times new roman", 15, "bold"), fg='black', bd=5, relief=GROOVE, command= lambda :delete_enterprise(self))
        self.deletebutton1.place(x=570, y=190, width=200)

        self.refreshbutton1 = Button(self.frame21, text="Refresh", font=("times new roman", 15, "bold"), fg='black', bd=5, relief=GROOVE, command = lambda :refresh1(self))
        self.refreshbutton1.place(x=850, y=190, width=200)

        self.frame22 = Frame(self.tab2, relief=FLAT, bg="#B0C4DE")
        self.frame22.place(x=5, y=270, width=1090, height=300)

        self.frame23 = Frame(self.frame22, relief=FLAT, bg="white")
        self.frame23.place(x=5, y=5, width=1080, height=55)

        self.frame24 = Frame(self.frame22, relief=FLAT, bg="white")
        self.frame24.place(x=5, y=60, width=1080, height=230)

        self.searchby1 = Label(self.frame23, text="Search: ", font=("Times new roman", 12, "bold"), fg="black",
                              bg="white")
        self.searchby1.place(x=100, y=10)

        d = ["Name", "Code", "Year","Type","Contact"]
        self.searchcombo1 = ttk.Combobox(self.frame23, values=d, font=("times new roman", 12, "bold"))
        self.searchcombo1.place(x=180, y=10, width=200)
        self.searchcombo1.set("Select option")
        self.searchcombo1.config(state="readonly")

        self.search_entry1 = Entry(self.frame23, font=("times new roman", 12, "bold"))
        self.search_entry1.place(x=400, y=10, width=250)

        self.searchbutton1 = Button(self.frame23, text="Search", font=("times new roman", 12, "bold"), fg='black', bg='#0080FF', bd=5, relief=GROOVE, command= lambda :search1(self))
        self.searchbutton1.place(x=700, y=10, width=100)

        self.showbutton1 = Button(self.frame23, text="Show", font=("times new roman", 12, "bold"), fg='black', bg='#0080FF', bd=5, relief=GROOVE, command= lambda :self.show1())
        self.showbutton1.place(x=900, y=10, width=100)

        self.tree_scroll1 = Scrollbar(self.frame24)
        self.treeview1 = ttk.Treeview(self.frame24, columns=(1, 2, 3, 4, 5, 6), show="headings", yscrollcommand=self.tree_scroll1.set)
        self.tree_scroll1.pack(side=RIGHT, fill=Y)
        self.tree_scroll1.config(command=self.treeview1.yview)

        self.treeview1.heading(1, text="Company's name")
        self.treeview1.heading(2, text="Business code")
        self.treeview1.heading(3, text="Founded year")
        self.treeview1.heading(4, text="Business type")
        self.treeview1.heading(5, text="Address")
        self.treeview1.heading(6, text="Contact")

        self.treeview1.column(1, width=175)
        self.treeview1.column(2, width=200)
        self.treeview1.column(3, width=150)
        self.treeview1.column(4, width=175)
        self.treeview1.column(5, width=175)
        self.treeview1.column(6, width=175)

        self.treeview1.place(x=5, y=0, width=1055)
        self.show1()

        #design tab3:
        self.label3 = Label(self.tab3, image=self.newbg0)
        self.label3.place(x=0, y=0)
        self.frame31 = Frame(self.tab3)
        self.frame31.place(x=750,y=0,width=300, height=300)
        self.bg1 = Image.open("hotline.jpg")
        self.resize1 = self.bg1.resize((300, 300), Image.ANTIALIAS)
        self.newbg1 = ImageTk.PhotoImage(self.resize1)
        self.label4 = Label(self.frame31, image=self.newbg1)
        self.label4.place(x=0, y=0)
        self.label5 = Label(self.tab3, text = "Phone number: ", font=("times new roman", 35, "bold"), bg ='white')
        self.label5.place(x=30, y=30)
        self.label6 = Label(self.tab3, text="01741476476", font=("times new roman", 35, "bold"), bg = "white")
        self.label6.place(x=30, y=200)
        self.label7 = Label(self.tab3, text="Email: ", font=("times new roman", 35, "bold"), bg= "white")
        self.label7.place(x=30, y=400)
        self.label8 = Label(self.tab3, text="gacon123@gmail.com", font=("times new roman", 35, "bold"), bg= "white")
        self.label8.place(x=30, y=500)



    #define function show
    def show(self):
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                         auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        command_handler.execute("SELECT * from information")
        self.row = command_handler.fetchall()
        if len(self.row) != 0:
            self.treeview.delete(*self.treeview.get_children())
            for i in self.row:
                self.treeview.insert('', 'end', values=i)
                db.commit()

    def showall(self):
            self.show()

    def show1(self):
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                         auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        command_handler.execute("SELECT * from enterprise")
        self.row1 = command_handler.fetchall()
        if len(self.row1) != 0:
            self.treeview1.delete(*self.treeview1.get_children())
            for i in self.row1:
                self.treeview1.insert('', 'end', values=i)
                db.commit()

    def showall1(self):
            self.show1()

    def exit(self):
        self.window.destroy()

    def read(self):
        self.newwindow = Toplevel(self.window)
        self.app = intro(self.newwindow)

