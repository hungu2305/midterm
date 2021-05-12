from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

root = Tk()
class mainwindow():
    def __init__(self):
        self.root = root
        self.root.title("PUBLIC GOVERNMENT SERVICE INFORMATION MANAGEMENT SYSTEM")
        self.root.geometry("1570x790")
        self.frame = Frame(self.root, bg="#0040FF", relief=FLAT)
        self.frame.place(x=0, y=0, width=1530, height=100)

        self.heading_label = Label(self.frame, text="PUBLIC GOVERNMENT SERVICE INFORMATION MANAGEMENT SYSTEM", fg='black', bg="#0040FF", font=('times new roman', 15, 'bold'))
        self.heading_label.place(x=0, y=0, width=1530)

        self.frame1 = Frame(self.root, bg="#B0C4DE", relief=FLAT)
        self.frame1.place(x=10, y=110, width=1090, height=330)

        self.label = Label(self.frame1, text="Citizen information", font=("times new roman", 15, "bold"), bg='black', fg="white")
        self.label.place(x=0, y=0, width=1090)

        self.firstname = Label(self.frame1, text="First name", font=("times new roman", 12, "bold"), fg="black", bg="#B0C4D3")
        self.firstname.place(x=30, y=50)

        self.fentry = Entry(self.frame1, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.fentry.place(x=30, y=90, width=250)

        self.lastname = Label(self.frame1, text="Last name", font=("times new roman", 12, "bold"), fg="black", bg="#B0C4D3")
        self.lastname.place(x=320, y=50)

        self.lentry = Entry(self.frame1, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.lentry.place(x=320, y=90, width=250)

        self.yob = Label(self.frame1, text="Year of birth", font=("times new roman", 12, "bold"), fg="black", bg="#B0C4D3")
        self.yob.place(x=600, y=50)

        self.year_choice = ttk.Spinbox(self.frame1, from_= 1950, to = 2021, font=("times new roman", 12, "bold"))
        self.year_choice.place(x=600, y=90, width=120)
        self.year_choice.config(state="readonly")
        self.year_choice.set("  -Select year-  ")

        self.cccd = Label(self.frame1, text="Citizen identification", font=("times new roman", 12, "bold"), fg="black", bg="#B0C4D3")
        self.cccd.place(x=30, y=150)

        self.cccd_entry = Entry(self.frame1, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.cccd_entry.place(x=30, y=190, width=250)

        self.where = Label(self.frame1, text="Home town", font=("times new roman", 12, "bold"), fg="black", bg="#B0C4D3")
        self.where.place(x=320, y=150)

        self.where_entry = Entry(self.frame1, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.where_entry.place(x=320, y=190, width=250)

        self.gender = Label(self.frame1, text="Gender", font=("times new roman", 12, "bold"), fg="black", bg="#B0C4D3")
        self.gender.place(x=600, y=150)

        a = ['Male', 'Female']
        self.gender_entry = ttk.Combobox(self.frame1, values=a, font=("times new roman", 12, "bold"))
        self.gender_entry.place(x=600, y=190, width=120)
        self.gender_entry.config(state="readonly")

        self.folk = Label(self.frame1, text="Folk", font=("times new roman", 12, "bold"), fg="black", bg="#B0C4D3")
        self.folk.place(x=30, y=240)

        self.folk_entry = Entry(self.frame1, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.folk_entry.place(x=30, y=280, width=120)

        self.contact = Label(self.frame1, text="Contact phone", font=("times new roman", 12, "bold"), fg="black", bg="#B0C4D3")
        self.contact.place(x=320, y=240)

        self.contact_entry = Entry(self.frame1, font=("times new roman", 12, "bold"), relief=RIDGE)
        self.contact_entry.place(x=320, y=280, width=250)

        self.marital = Label(self.frame1, text="Marital status", font=("times new roman", 12, "bold"), fg="black", bg="#B0C4D3")
        self.marital.place(x=600, y=240)

        b = ['Single', 'Married', 'Divorced']
        self.marital_choice = ttk.Combobox(self.frame1, values=b, font=("times new roman", 12, "bold"))
        self.marital_choice.place(x=600, y=280, width=120)
        self.marital_choice.config(state="readonly")

        self.addbutton = Button(self.frame1, text="Add", font=("times new roman", 15, "bold"), fg='black', bg='#0080FF',bd=5, relief=GROOVE, command=lambda:self.add_citizen())
        self.addbutton.place(x=770, y=60, width=200)

        self.updatebutton = Button(self.frame1, text="Update", font=("times new roman", 15, "bold"), fg='black', bg='#0080FF', bd=5, relief=GROOVE, command=lambda :self.update_citizen())
        self.updatebutton.place(x=770, y=130, width=200)

        self.deletebutton = Button(self.frame1, text="Delete", font=("times new roman", 15, "bold"), fg='black', bg='#0080FF', bd=5, relief=GROOVE, command=lambda:self.delete_citizen())
        self.deletebutton.place(x=770, y=200, width=200)

        self.refreshbutton = Button(self.frame1, text="Refresh", font=("times new roman", 15, "bold"), fg='black', bg='#0080FF', bd=5, relief=GROOVE, command=lambda:self.refresh())
        self.refreshbutton.place(x=770, y=270, width=200)

        self.frame2=Frame(self.root, relief=FLAT, bg="#B0C4DE")
        self.frame2.place(x=1110, y=110, width=410, height=330)

        self.frame3=Frame(self.root, relief=FLAT, bg="#B0C4DE")
        self.frame3.place(x=10, y = 450,width=1510, height=330)

        self.frame4=Frame(self.frame3, relief=FLAT, bg="white")
        self.frame4.place(x=5,y=5, width=1495, height=55)

        self.searchby = Label(self.frame4, text="Search: ", font=("Times new roman", 12, "bold"), fg="black", bg="white")
        self.searchby.place(x=200, y=10)

        c = ["Lastname", "CI", "Contact"]
        self.searchcombo = ttk.Combobox(self.frame4, values=c, font=("times new roman", 12, "bold"))
        self.searchcombo.place(x=350, y=10, width=200)
        self.searchcombo.set("Select option")
        self.searchcombo.config(state="readonly")

        self.search_entry = Entry(self.frame4, font=("times new roman", 12, "bold"))
        self.search_entry.place(x=600, y=10, width=250)

        self.searchbutton = Button(self.frame4, text="Search", font=("times new roman", 12, "bold"), fg='black', bg='#0080FF', bd=5, relief=GROOVE, command=lambda:self.search())
        self.searchbutton.place(x=900, y=10, width=100)

        self.showbutton = Button(self.frame4, text="Show", font=("times new roman", 12, "bold"), fg='black', bg='#0080FF', bd=5, relief=GROOVE, command=lambda:self.showall())
        self.showbutton.place(x=1100, y=10, width=100)

        self.scrollx = ttk.Scrollbar(self.frame3, orient=VERTICAL)
        self.scrolly = ttk.Scrollbar(self.frame3, orient=HORIZONTAL)
        self.treeview=ttk.Treeview(self.frame3, columns=(1,2,3,4,5,6,7,8,9), show="headings", height=11, xscrollcommand=self.scrollx.set(1,1000), yscrollcommnad=self.scrolly.set(1,1000))
        self.scrollx.pack(side=RIGHT, fill=Y)
        self.scrolly.pack(side=BOTTOM, fill=X)

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

        self.treeview.place(x=5,y=65, width=1485)
        self.show()

    def add_citizen(self):
        if self.fentry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.lentry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.year_choice.get()=="  -Select year-  ":
            messagebox.showerror("Error", "All fields are required!")
        elif self.cccd_entry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.where_entry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.gender_entry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.folk_entry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.contact_entry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.marital_choice.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        else:
            db = mysql.connector.connect(user='root',password='Uyenhung2596',host='localhost',database='midterm',auth_plugin='mysql_native_password')
            command_handler = db.cursor()
            querry_vals = (self.fentry.get(),self.lentry.get(),self.year_choice.get(),self.cccd_entry.get(),self.where_entry.get(),self.gender_entry.get(),self.folk_entry.get(),self.contact_entry.get(),self.marital_choice.get())
            command_handler.execute("INSERT INTO information(Firstname, Lastname, Year_of_birth, Citizen_Identification, Home_town, Gender, Folk, Contact_phone, Marital_status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",querry_vals)
            db.commit()
            db.close()
            messagebox.showinfo("Success", "Added Successfully")

    def update_citizen(self):
        if self.fentry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.lentry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.year_choice.get()=="  -Select year-  ":
            messagebox.showerror("Error", "All fields are required!")
        elif self.cccd_entry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.where_entry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.gender_entry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.folk_entry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.contact_entry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.marital_choice.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        else:
            db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm', auth_plugin='mysql_native_password')
            command_handler = db.cursor()
            querry_vals = (self.fentry.get(),self.lentry.get(),self.year_choice.get(),self.cccd_entry.get(),self.where_entry.get(),self.gender_entry.get(),self.folk_entry.get(),self.contact_entry.get(),self.marital_choice.get())
            command_handler.execute("UPDATE information set Firstname=%s, Lastname=%s, Year_of_birth=%s, Citizen_Identification=%s, Home_town=%s, Gender=%s, Folk=%s, Contact_phone=%s, Marital_status=%s",querry_vals)
            db.commit()
            db.close()
            messagebox.showinfo("Success", "Updated Successfully")

    def delete_citizen(self):
        if self.cccd_entry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        else:
            db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm', auth_plugin='mysql_native_password')
            command_handler = db.cursor()
            idcheck=(self.cccd_entry.get(),)
            command_handler.execute("DELETE from information WHERE Citizen_Identification= %s", idcheck)
            db.commit()
            db.close()
            messagebox.showinfo("Success", "Deleted Successfully")

    def refresh(self):
        self.fentry.delete(0,END)
        self.lentry.delete(0,END)
        self.year_choice.set("  -Select year-  ")
        self.cccd_entry.delete(0,END)
        self.where_entry.delete(0,END)
        self.gender_entry.set("")
        self.folk_entry.delete(0,END)
        self.contact_entry.delete(0,END)
        self.marital_choice.set("")

    def show(self):
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm', auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        command_handler.execute("SELECT * from information")
        self.row=command_handler.fetchall()
        if len(self.row) !=0:
            self.treeview.delete(*self.treeview.get_children())
            for i in self.row:
                self.treeview.insert('','end',values=i)
                db.commit()

    def search(self):
        if self.searchcombo.get()=="Lastname":
            db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',auth_plugin='mysql_native_password')
            command_handler = db.cursor()
            command_handler.execute("SELECT * from information where Lastname=%s",(self.search_entry.get(),))
            self.row = command_handler.fetchall()
            if len(self.row) != 0:
                self.treeview.delete(*self.treeview.get_children())
                for i in self.row:
                    self.treeview.insert('', 'end', values=i)
                    db.commit()
        elif self.searchcombo.get()=="CI":
            db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',auth_plugin='mysql_native_password')
            command_handler = db.cursor()
            command_handler.execute("SELECT * from information where Citizen_Identification=%s",(self.search_entry.get(),))
            self.row = command_handler.fetchall()
            if len(self.row) != 0:
                self.treeview.delete(*self.treeview.get_children())
                for i in self.row:
                    self.treeview.insert('', 'end', values=i)
                    db.commit()
        elif self.searchcombo.get()=="Contact":
            db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',auth_plugin='mysql_native_password')
            command_handler = db.cursor()
            command_handler.execute("SELECT * from information where Contact_phone=%s",(self.search_entry.get(),))
            self.row = command_handler.fetchall()
            if len(self.row) != 0:
                self.treeview.delete(*self.treeview.get_children())
                for i in self.row:
                    self.treeview.insert('', 'end', values=i)
                    db.commit()
        else:
            messagebox.showerror("Error","Please select true option")

    def showall(self):
        self.show()



m = mainwindow()
root.mainloop()
