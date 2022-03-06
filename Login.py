from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from sqlite3 import *
import home

class Loginwindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title('Login')
        self.geometry('300x300')

        s= Style()
        s.configure('hf.TFrame', background= 'blue')
        
        hf= Frame(self, style= 'hf.TFrame')
        hf.pack(fill= X)

        s.configure('hf.TLabel', background= 'blue', foreground= 'white', font= ('Arial', 25))

        hl= Label(hf, text= 'My Contact Book', style= 'hf.TLabel')
        hl.pack(pady= 10)

        cf= Frame(self, style= 'cf.TFrame')
        cf.pack(fill= BOTH, expand= True)

        s.configure('cf.TFrame', background= 'white')


        lf= Frame(cf, style= 'cf.TFrame')
        lf.place(relx= .5, rely= .5, anchor= CENTER)

        username_label= Label(lf, text= 'Username: ', style= 'lf.TLabel')
        username_label.grid(row= 0, column= 0)

        self.username_entry= Entry(lf, font= ('Arial', 11), width= 15)
        self.username_entry.grid(row= 0, column= 1, pady= 5)

        password_label= Label(lf, text= 'Password: ', style= 'lf.TLabel')
        password_label.grid(row= 1, column= 0)

        self.password_entry= Entry(lf, font= ('Arial', 11), width= 15, show= '*')
        self.password_entry.grid(row= 1, column= 1, pady= 5)

        s.configure('lf.TLabel', background= 'white', font= ('Arial', 11))

        login_button= Button(lf, text= 'Login', width= 15, style= 'lf.TButton', command= self.login_button_click)
        login_button.grid(row= 2, column= 1, pady= 5)

        s.configure('lf.TButton', font= ('Arial', 11))

    def login_button_click(self):
        con= connect('contacts.db')
        cur= con.cursor()
        cur.execute('select * from login where Username= ? and Password= ?', (self.username_entry.get(), self.password_entry.get()))
        row= cur.fetchone()
        if row is not None:
            self.destroy()
            home.Homewindow()
        else:
            messagebox.showerror('Error', 'Invalid username/Password')
        

if __name__ == '__main__':
    w= Loginwindow()
    w.mainloop()

    
