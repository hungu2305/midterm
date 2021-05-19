import mysql.connector
from tkinter import messagebox

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