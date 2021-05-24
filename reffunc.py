from tkinter import *
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