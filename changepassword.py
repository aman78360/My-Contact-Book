from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from sqlite3 import *

class Changepasswordframe(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.place(relx= .5, rely= .5, anchor= CENTER)

        s= Style()

        s.configure('TFrame', background= 'white')
        s.configure('TLabel', background= 'white', font= ('Arial', 11))
        s.configure('TButton', font= ('Arial', 11))


        opl= Label(self, text= 'Old Password', style= 'TLabel')
        opl.grid(row= 0, column= 0, sticky= W)

        self.ope= Entry(self, font= ('Arial', 11), width= 20, show= '*')
        self.ope.grid(row= 0, column= 1, pady= 5)

        npl= Label(self, text= 'New Password', style= 'TLabel')
        npl.grid(row=1, column= 0, sticky= W)

        self.npe= Entry(self, font= ('Arial', 11), width= 20, show= '*')
        self.npe.grid(row= 1, column= 1, pady= 5)

        cpl= Label(self, text= 'Confirm Password', style= 'TLabel')
        cpl.grid(row= 2, column= 0, sticky= W)

        self.cpe= Entry(self, font= ('Arial', 11), width= 20, show= '*')
        self.cpe.grid(row= 2, column= 1, pady= 5)

        cpb= Button(self, text= 'Change Password', width= 20, command= self.change_password_button_click)
        cpb.grid(row= 3, column= 1, pady= 5)

    def change_password_button_click(self):
        con= connect('contacts.db')
        cur= con.cursor()
        cur.execute('select * from login where Password= ?', (self.ope.get(),))
        row= cur.fetchone()
        if row is not None:
            if self.npe.get()== self.cpe.get():
                cur.execute('update login set Password= ? where Password=?', (self.npe.get(), self.ope.get()))
                con.commit()
                messagebox.showinfo('success', 'Password changed successfully')
            else:
                messagebox.showerror('Error', 'Password does not match')
        else:
            messagebox.showerror('Error', 'Incorrect Old Password')
