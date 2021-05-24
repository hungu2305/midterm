from tkinter import *
from tkinter import messagebox
import mysql.connector

def add_citizen(self):
    if self.fentry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.lentry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.year_choice.get() == "  -Select year-  ":
        messagebox.showerror("Error", "All fields are required!")
    elif self.cccd_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.where_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.gender_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.folk_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.contact_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.marital_choice.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    else:
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                     auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        querry_vals = (
        self.fentry.get(), self.lentry.get(), self.year_choice.get(), self.cccd_entry.get(), self.where_entry.get(),
        self.gender_entry.get(), self.folk_entry.get(), self.contact_entry.get(), self.marital_choice.get())
        command_handler.execute(
            "INSERT INTO information(Firstname, Lastname, Year_of_birth, Citizen_Identification, Home_town, Gender, Folk, Contact_phone, Marital_status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            querry_vals)
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Added Successfully")

def update_citizen(self):
    if self.fentry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.lentry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.year_choice.get() == "  -Select year-  ":
        messagebox.showerror("Error", "All fields are required!")
    elif self.cccd_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.where_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.gender_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.folk_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.contact_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    elif self.marital_choice.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    else:
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                     auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        querry_vals = (
        self.fentry.get(), self.lentry.get(), self.year_choice.get(), self.where_entry.get(), self.gender_entry.get(),
        self.folk_entry.get(), self.contact_entry.get(), self.marital_choice.get(), self.cccd_entry.get())
        command_handler.execute(
            "UPDATE information set Firstname=%s, Lastname=%s, Year_of_birth=%s, Home_town=%s, Gender=%s, Folk=%s, Contact_phone=%s, Marital_status=%s where Citizen_Identification=%s",
            querry_vals)
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Updated Successfully")

def delete_citizen(self):
    if self.cccd_entry.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    else:
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                     auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        idcheck = (self.cccd_entry.get(),)
        command_handler.execute("DELETE from information WHERE Citizen_Identification= %s", idcheck)
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Deleted Successfully")

def search(self):
    if self.searchcombo.get() == "Lastname":
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                     auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        command_handler.execute("SELECT * from information where Lastname=%s", (self.search_entry.get(),))
        self.row = command_handler.fetchall()
        if len(self.row) != 0:
            self.treeview.delete(*self.treeview.get_children())
            for i in self.row:
                self.treeview.insert('', 'end', values=i)
                db.commit()
    elif self.searchcombo.get() == "CI":
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                     auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        command_handler.execute("SELECT * from information where Citizen_Identification=%s", (self.search_entry.get(),))
        self.row = command_handler.fetchall()
        if len(self.row) != 0:
            self.treeview.delete(*self.treeview.get_children())
            for i in self.row:
                self.treeview.insert('', 'end', values=i)
                db.commit()
    elif self.searchcombo.get() == "Contact":
        db = mysql.connector.connect(user='root', password='Uyenhung2596', host='localhost', database='midterm',
                                     auth_plugin='mysql_native_password')
        command_handler = db.cursor()
        command_handler.execute("SELECT * from information where Contact_phone=%s", (self.search_entry.get(),))
        self.row = command_handler.fetchall()
        if len(self.row) != 0:
            self.treeview.delete(*self.treeview.get_children())
            for i in self.row:
                self.treeview.insert('', 'end', values=i)
                db.commit()
    else:
        messagebox.showerror("Error", "Please select true option")

def refresh(self):
    self.fentry.delete(0, END)
    self.lentry.delete(0, END)
    self.year_choice.set("  -Select year-  ")
    self.cccd_entry.delete(0, END)
    self.where_entry.delete(0, END)
    self.gender_entry.set("")
    self.folk_entry.delete(0, END)
    self.contact_entry.delete(0, END)
    self.marital_choice.set("")