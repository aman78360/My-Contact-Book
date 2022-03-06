from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import Login
import changepassword
import managecontacts
class Homewindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title('Home')
        self.state('zoomed')
        s= Style()
        s.configure('hf.TFrame', background= 'blue')

        hf= Frame(self, style= 'hf.TFrame')
        hf.pack(fill= X)

        s.configure('hl.TLabel', background= 'blue', foreground= 'white', font= ('Arial', 25))

        hl= Label(hf, text= 'My Contact Book', style= 'hl.TLabel')
        hl.pack(pady= 10)

        nf= Frame(self, style= 'hf.TFrame')
        nf.pack(fill= Y, side= LEFT)

        s.configure('nf.TButton', font= ('Arial', 11))

        mcb= Button(nf, text= 'Manage Contacts', width= 20, style= 'nf.TButton', command= self.manage_contacts_button_click)
        mcb.pack(pady= 1, ipady= 8)

        cpb= Button(nf, text= 'Change Password', width= 20, style= 'nf.TButton', command= self.change_password_button_click)
        cpb.pack(pady= 1, ipady= 8)

        lb= Button(nf, text= 'Logout', width= 20, style= 'nf.TButton', command= self.logout_button_click)
        lb.pack(pady= 1, ipady= 8)

        s.configure('cf.TFrame', background= 'white')

        self.cf= Frame(self, style= 'cf.TFrame')
        self.cf.pack(fill= BOTH, expand= TRUE)

        managecontacts.Managecontactframe(self.cf)

        
    def logout_button_click(self):
        self.destroy()
        Login.Loginwindow()

    def change_password_button_click(self):
        for inner_frame in self.cf.winfo_children():
            inner_frame.destroy()
        changepassword.Changepasswordframe(self.cf)

    def manage_contacts_button_click(self):
        for inner_frame in self.cf.winfo_children():
            inner_frame.destroy()
        managecontacts.Managecontactframe(self.cf)
        
