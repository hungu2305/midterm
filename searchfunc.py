from tkinter import *
from tkinter import messagebox
import mysql.connector
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