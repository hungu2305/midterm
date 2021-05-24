from tkinter import *
from tkinter import messagebox
import mysql.connector


def add_enterprise(self):
    if self.name_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.code_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.year_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.type_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.address_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.phone_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    else:
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                     auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        vals = (self.name_entry.get(), self.code_entry.get(), self.year_entry.get(), self.type_entry.get(),
                self.address_entry.get(), self.phone_entry.get())
        command_handler.execute(
            "INSERT INTO enterprise(CompanyName, BusinessCode, FoundedYear, BusinessType, Address, Contact) VALUES (%s, %s, %s, %s, %s, %s)",
            vals)
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Added Successfully")

def update_enterprise(self):
    if self.name_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.code_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.year_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.type_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.address_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.phone_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    else:
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                     auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        vals = (self.name_entry.get(), self.year_entry.get(), self.type_entry.get(),
                self.address_entry.get(), self.phone_entry.get(), self.code_entry.get())
        command_handler.execute("UPDATE enterprise set CompanyName=%s, FoundedYear=%s, BusinessType=%s, Address=%s, Contact=%s where BusinessCode= %s", vals)
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Updated Successfully")

def delete_enterprise(self):
    if self.code_entry.get() == "":
        messagebox.showerror("Error", "Code field are required!")
    else:
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                     auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        codecheck = (self.code_entry.get(),)
        command_handler.execute("DELETE from enterprise WHERE BusinessCode= %s", codecheck)
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Deleted Successfully")

def search1(self):
    if self.searchcombo1.get() == "Name":
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                     auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        command_handler.execute("SELECT * from enterprise where CompanyName=%s", (self.search_entry1.get(),))
        self.row1 = command_handler.fetchall()
        if len(self.row1) != 0:
            self.treeview1.delete(*self.treeview1.get_children())
            for i in self.row1:
                self.treeview1.insert('', 'end', values=i)
                db.commit()
    elif self.searchcombo1.get() == "Code":
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                     auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        command_handler.execute("SELECT * from enterprise where BusinessCode=%s", (self.search_entry1.get(),))
        self.row1 = command_handler.fetchall()
        if len(self.row1) != 0:
            self.treeview1.delete(*self.treeview1.get_children())
            for i in self.row1:
                self.treeview1.insert('', 'end', values=i)
                db.commit()
    elif self.searchcombo1.get() == "Year":
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                     auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        command_handler.execute("SELECT * from enterprise where FoundedYear=%s", (self.search_entry1.get(),))
        self.row1 = command_handler.fetchall()
        if len(self.row1) != 0:
            self.treeview1.delete(*self.treeview1.get_children())
            for i in self.row1:
                self.treeview1.insert('', 'end', values=i)
                db.commit()
    elif self.searchcombo1.get() == "Type":
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                     auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        command_handler.execute("SELECT * from enterprise where BusinessType=%s", (self.search_entry1.get(),))
        self.row1 = command_handler.fetchall()
        if len(self.row1) != 0:
            self.treeview1.delete(*self.treeview1.get_children())
            for i in self.row1:
                self.treeview1.insert('', 'end', values=i)
                db.commit()
    elif self.searchcombo1.get() == "Contact":
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                     auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        command_handler.execute("SELECT * from enterprise where Contact=%s", (self.search_entry1.get(),))
        self.row1 = command_handler.fetchall()
        if len(self.row1) != 0:
            self.treeview1.delete(*self.treeview1.get_children())
            for i in self.row1:
                self.treeview1.insert('', 'end', values=i)
                db.commit()
    else:
        messagebox.showerror("Error", "Please select true option")

def refresh1(self):
    self.name_entry.delete(0, END)
    self.code_entry.delete(0, END)
    self.year_entry.delete(0,END)
    self.type_entry.delete(0, END)
    self.address_entry.delete(0, END)
    self.phone_entry.delete(0, END)