from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from main import windowclass

class login:
    def __init__(self, login):
        self.login = login
        self.login.title("Login System")
        self.login.geometry("900x500")
        self.bg = Image.open("login.jpg")
        self.resize = self.bg.resize((900,500), Image.ANTIALIAS)
        self.newbg = ImageTk.PhotoImage(self.resize)
        self.canvas = Canvas(self.login)
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.create_image(0,0, image=self.newbg, anchor=NW)

        self.logframe = Frame(self.login, bg= "white")
        self.logframe.place(x=100,y=90,height=340, width=500)
        self.title = Label(self.logframe, text="Login here", font=("times new roman",20, 'bold'), fg="#d77337", bg="white")
        self.title.place(x=50,y=50)

        self.user = Label(self.logframe, text="Username", font=("times new roman",18, 'bold'), fg="black", bg="white")
        self.user.place(x=50, y=100)
        self.user_entry = Entry(self.logframe, font=("times new roman", 15, 'bold'), fg='black', bg="white")
        self.user_entry.place(x=50, y=150, width=250)

        self.password = Label(self.logframe, text="Password", font=("times new roman",18, 'bold'), fg="black", bg="white")
        self.password.place(x=50,y=200)
        self.password_entry = Entry(self.logframe, font=("times new roman", 15, 'bold'), fg='black', bg="white", show="*")
        self.password_entry.place(x=50, y=250,width=250)

        self.button = Button(self.login, text='Login', command=lambda :self.check())
        self.button.place(x=310,y=450)

    def check(self):
        if self.user_entry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.password_entry.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        else:
            if self.user_entry.get()=="username" and self.password_entry.get()=="123456":
                root = Toplevel()
                root.title("PUBLIC GOVERNMENT SERVICE INFORMATION MANAGEMENT SYSTEM")
                root.geometry("1110x650")
                c = windowclass(root)
                root.mainloop()
            else:
                messagebox.showerror("Error", "Wrong username or password, please login again!")


root0 = Tk()
obj = login(root0)
root0.mainloop()