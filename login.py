from tkinter import *
from tkinter import messagebox, filedialog
import sqlite3 as sql
from PIL import ImageTk, Image

#login() function is to create the login window where end user enters username and password to login.
def login():
    
    log = Tk()
    log.title('Login to BMS')
    log.geometry("310x330+510+180")
    log.resizable(width=False, height=False)
    log.configure(bg='#DDDD88')

#check() function is to verify username and password entred and checks if the username exists or not.
    
    #def redirect(event):
    #    check()

    def check():
        if len(E1.get())==0:
            messagebox.showinfo('Violation','Username cannot be empty')
        elif len(E2.get())==0:
            messagebox.showinfo('Violation','Password cannot be empty')
        else:
            user = E1.get()
            pas = E2.get()
            con = sql.connect('project.db')
            c = con.cursor()

            if user=='admin' and pas=='admin':
                from after_login import a_log
                log.destroy()
                a_log()
            elif user=='admin' and pas!='admin':
                messagebox.showwarning('Unsuccessful','Your password is NOT correct')
            elif user!='admin':
                for i in c.execute('SELECT * FROM users'):
                    if user == i[5] and pas == i[6]:
                        from after_login import local_log
                        log.destroy()
                        local_log()
                        break
                    elif user == i[5] and pas != i[6]:
                        messagebox.showwarning('Unsuccessful','Your password is NOT correct')
                        break
                    elif user != i[5] and pas != i[6]:
                        messagebox.showwarning('Unsuccessful','Your username is NOT correct')
                        print("Break")
                        break
            con.close()

        
    L1 = Label(log, text="Username", font=('Arial',10),bg='#DDDD88')
    E1 = Entry(log, bd=3, width=26, )
    L2 = Label(log, text="Password", font=('Arial',10),bg='#DDDD88')
    E2 = Entry(log, bd=3, width=26, show='*')

    L4 = Label(log, bg='#DDDD88')
    L5 = Label(log, bg='#DDDD88')
    L6 = Label(log, bg='#DDDD88')
    L7 = Label(log, bg='#DDDD88')
    
    B1 = Button(log, text='LOGIN', width=12, bg="lightgreen", font=('Comic Sans MS',8), command=check)
    B2 = Button(log, text='CANCEL', width=12, bg='pink', fg='maroon', font=('Comic Sans MS',8), command=log.destroy)

    
    L4.pack()
    L1.pack()
    E1.pack()
    L5.pack()
    L2.pack()
    E2.pack()
    L6.pack()
    B1.pack()
    L7.pack()
    #L3.pack()
    B2.pack()

    #log.bind('<Return>', redirect)
    log.mainloop()

#login()
