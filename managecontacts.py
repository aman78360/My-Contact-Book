from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from sqlite3 import *

class Managecontactframe(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.pack(fill= BOTH, expand= TRUE)

        s= Style()
        s.configure('TFrame', background = 'white')
        s.configure('TLabel', background = 'white', font = ('Arial', 11))
        s.configure('TButton', font = ('Arial', 11))

        self.con= connect('contacts.db')
        self.cur= self.con.cursor()

        self.viewallcontactframe()

    def viewallcontactframe(self):

        self.vacf= Frame(self)
        self.vacf.place(relx= 0.5, rely= 0.5, anchor= CENTER)

        ancb= Button(self.vacf, text= 'Add New Contact', command= self.add_new_contact_button_click)
        ancb.grid(row= 0, column= 0, sticky= E, pady= 25, columnspan= 2)

        nl= Label(self.vacf, text= 'Name: ')
        nl.grid(row= 1, column= 0)

        self.ne= Entry(self.vacf, font = ('Arial', 11), width= 68)
        self.ne.grid(row= 1, column= 1, pady= 10)
        self.ne.bind('<KeyRelease>', self.name_entry_key_released)

        self.vctv= Treeview(self.vacf, columns= ('name', 'phone_no', 'email_id', 'city'), show= 'headings')
        self.vctv.grid(row= 2, column= 0, columnspan= 2, pady= 10)

        self.vctv.heading('name', text= 'Name')
        self.vctv.heading('phone_no', text= 'Phone Number')
        self.vctv.heading('email_id', text= 'Email Id')
        self.vctv.heading('city', text= 'City')
        self.vctv.column('name', width= 200)
        self.vctv.column('phone_no', width= 100)
        self.vctv.column('email_id', width= 200)
        self.vctv.column('city', width= 100)
        self.vctv.bind('<<TreeviewSelect>>', self.contacts_treeview_row_selection)

        self.cur.execute('select * from mycontacts')
        self.fill_contacts_treeview()

    def fill_contacts_treeview(self):

        for contact in self.vctv.get_children():
            self.vctv.delete(contact)
            
        contacts= self.cur.fetchall()
        for contact in contacts:
            self.vctv.insert('', END, values= contact)

    def add_new_contact_button_click(self):
        self.vacf.destroy()
        self.ancf= Frame(self)
        self.ancf.place(relx= 0.5, rely= 0.5, anchor= CENTER)

        nl= Label(self.ancf, text= 'Name: ')
        nl.grid(row= 0, column= 0, sticky= W)

        self.ne= Entry(self.ancf, width= 20, font = ('Arial', 11))
        self.ne.grid(row= 0, column= 1, pady= 10)

        pnl= Label(self.ancf, text= 'Phone Number: ')
        pnl.grid(row= 1, column= 0, sticky= W)

        self.pne= Entry(self.ancf, width= 20,font = ('Arial', 11))
        self.pne.grid(row= 1, column= 1, pady= 10)

        eil = Label(self.ancf, text = "Email Id: ")
        eil.grid(row = 2, column = 0, sticky = W)

        self.eie = Entry(self.ancf, width = 20, font = ('Arial', 11))
        self.eie.grid(row = 2, column = 1, pady = 10)

        cl = Label(self.ancf, text = "City: ")
        cl.grid(row = 3, column = 0, sticky = W)

        self.ccb= Combobox(self.ancf, values= ('Noida', 'New Delhi', 'Banglore', 'Greater Noida', 'Pune', 'Mumbai'),
        width= 18, font = ('Arial', 11))
        self.ccb.grid(row= 3, column= 1)

        ab= Button(self.ancf, text= 'Add', width= 20, command= self.add_button_click)
        ab.grid(row= 4, column= 1, pady= 10)

    def add_button_click(self):

        self.cur.execute('select * from mycontacts where emailid= ?', (self.eie.get(),))
        email= self.cur.fetchone()

        if email is None:
            self.cur.execute('insert into mycontacts values(?, ?, ?, ?)', (self.ne.get(), self.pne.get(),
            self.eie.get(), self.ccb.get()))
            self.con.commit()
            messagebox.showinfo('Successfull', 'Contact added successfully')
            self.ancf.destroy()
            self.viewallcontactframe()
        else:
            messagebox.showerror('Error', 'Contact is already added')


    def name_entry_key_released(self, event):
         self.cur.execute('select * from mycontacts where name like ?', ('%'+ self.ne.get()+ '%',))
         self.fill_contacts_treeview()

    def contacts_treeview_row_selection(self, event):
        
        contact= self.vctv.item(self.vctv.selection())['values']
        self.vacf.destroy()
        self.udcf= Frame(self)
        self.udcf.place(relx= .5, rely= .5, anchor= CENTER)
            

        nl= Label(self.udcf, text= 'Name: ')
        nl.grid(row= 0, column= 0, sticky= W)

        self.ne= Entry(self.udcf, width= 20, font = ('Arial', 11))
        self.ne.grid(row= 0, column= 1, pady= 10)
        self.ne.insert(END, contact[0])

        pnl= Label(self.udcf, text= 'Phone Number: ')
        pnl.grid(row= 1, column= 0, sticky= W)

        self.pne= Entry(self.udcf, width= 20,font = ('Arial', 11))
        self.pne.grid(row= 1, column= 1, pady= 10)
        self.pne.insert(END, contact[1])

        eil = Label(self.udcf, text = "Email Id: ")
        eil.grid(row = 2, column = 0, sticky = W)

        self.eie = Entry(self.udcf, width = 20, font = ('Arial', 11))
        self.eie.grid(row = 2, column = 1, pady = 10)
        self.eie.insert(END, contact[2])
        self.email_id= contact[2]

        cl = Label(self.udcf, text = "City: ")
        cl.grid(row = 3, column = 0, sticky = W)

        self.ccb= Combobox(self.udcf, values= ('Noida', 'New Delhi', 'Banglore', 'greater Noida', 'Pune', 'Mumbai'),
        width= 18, font = ('Arial', 11))
        self.ccb.grid(row= 3, column= 1)
        self.ccb.set(contact[3])


        ub= Button(self.udcf, text= 'Update', width= 20, command= self.update_button_click)
        ub.grid(row= 4, column= 1, pady= 10)

        db= Button(self.udcf, text= 'Delete', width= 20, command= self.delete_button_click)
        db.grid(row= 5, column= 1, pady= 10)


    def update_button_click(self):
        self.cur.execute('update mycontacts set name= ?, phonenumber= ?, emailid= ?, city= ? where emailid= ?',
        (self.ne.get(), self.pne.get(), self.eie.get(), self.ccb.get(), self.email_id))
        self.con.commit()
        messagebox.showinfo('success', 'Contact has been updated successfully')
        self.udcf.destroy()
        self.viewallcontactframe()

    def delete_button_click(self):
        if messagebox.askquestion('Confirmation', 'Are you sure you want to delete this contact?')== 'yes':
            self.cur.execute('delete from mycontacts where emailid= ?', (self.email_id,))
            self.con.commit()
            messagebox.showinfo('Success', 'Contact has been deleted successfully')
        self.udcf.destroy()
        self.viewallcontactframe()


        
        




























        
        
