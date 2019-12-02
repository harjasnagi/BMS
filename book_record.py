from tkinter import *
from tkinter import messagebox, filedialog
import sqlite3 as sql
import tkinter
from PIL import ImageTk, Image

#submit() function creates a window named 'win' in which the details of requested book are entered.
def submit():
	win = Tk()
	win.title('Add book details')
	win.geometry("600x400+400+180")
	win.configure(bg='#DDDD88')

#check() function inside submit() checks for empty entries.
	def check():
		if len(E1.get())==0:
			messagebox.showinfo('Violation','ID cannot be empty')
		elif len(E2.get())==0:
			messagebox.showinfo('Violation','Name cannot be empty')
		elif len(E3.get())==0:
			messagebox.showinfo('Violation','Author cannot be empty')
		elif len(E4.get())==0:
			messagebox.showinfo('Violation','Enter valid price')
		else:
			upload()

#upload() function inside submit() uploads request to sql database if the check() returns true.
	def upload():

		idd = E1.get()
		name = E2.get()
		author = E3.get()
		price = E4.get()
		conn = sql.connect('project.db')
		c = conn.cursor()
		c.execute('CREATE TABLE IF NOT EXISTS books(Id,Name,Author,Price)')
		#c.fetchone()[0]
		c.execute('INSERT INTO books VALUES (?,?,?,?)',(idd,name, author, price))
		conn.commit()
		messagebox.showinfo('Success','Record added successfully to BMS')

	L = Label(win, text='Enter Book Details', font=('Comic Sans MS',14), bg='#DDDD88')
	L1 = Label(win, text='ID', font=('Arial',11), bg='#DDDD88')
	L2 = Label(win, text='Name', font=('Arial',11), bg='#DDDD88')
	L3 = Label(win, text='Author', font=('Arial',11), bg='#DDDD88')
	L4 = Label(win, text='Price', font=('Arial',11), bg='#DDDD88')
	E1 = Entry(win, bd=4)
	E2 = Entry(win, bd=4, width=50)
	E3 = Entry(win, bd=4, width=50)
	E4 = Entry(win, bd=4)
	B = Button(win, text='Submit', width=13, bg='lightgreen', command=check, bd=3)

	L.place(x=160,y=27)
	L1.place(x=100,y=90)
	E1.place(x=200,y=90)
	L2.place(x=100,y=140)
	E2.place(x=200,y=140)
	L3.place(x=100,y=190)
	E3.place(x=200,y=190)
	L4.place(x=100,y=240)
	E4.place(x=200,y=240)
	B.place(x=220,y=310)

	win.mainloop()

#submit()