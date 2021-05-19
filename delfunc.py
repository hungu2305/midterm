import mysql.connector
from tkinter import messagebox


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