from tkinter import *
from tkinter import messagebox, filedialog
import sqlite3 as sql
import tkinter
from PIL import ImageTk, Image

###############################################################################################################
##                                                                                                           ##
###                                                                                                         ###
####    The following code contains window of admin ( a_log() ) and local user ( local_log() )             ####
###                                                                                                         ###
##                                                                                                           ##
###############################################################################################################


# Functions inside a_log() function:
# users
# del_users
#
#
def a_log():

    admin_log = Tk()
    admin_log.title('BMS')
    admin_log.geometry("410x390+500+130")
	
    def users():

        con = sql.connect('project.db')
        c = con.cursor()
        show = Tk()
        show.title('USERS')
        show.geometry("800x500+300+100")

        TL1 = Label(show,text='----------------------------------------------------------------------------------------------------------------------------------------------------------')
        TL2 = Label(show,text='----------------------------------------------------------------------------------------------------------------------------------------------------------')
        TL7 = Label(show,text='Name')
        TL8 = Label(show,text='Email')
        TL9 = Label(show,text='Gender')
        TL10 = Label(show,text='Mobile')
        TL11 = Label(show,text='Address')
        TL12 = Label(show,text='Username')
        TL13 = Label(show,text='Password')
        TL1.place(x=10,y=10)
        TL2.place(x=10,y=50)
        TL7.place(x=30,y=35)
        TL8.place(x=140,y=35)
        TL9.place(x=250,y=35)
        TL10.place(x=320,y=35)
        TL11.place(x=450,y=35)
        TL12.place(x=550,y=35)
        TL13.place(x=670,y=35)

        no = 0
        for i in c.execute('SELECT * FROM users'):
            EL1 = Label(show,text=i[0])
            EL2 = Label(show,text=i[1])
            EL3 = Label(show,text=i[2])
            EL4 = Label(show,text=i[3])
            EL5 = Label(show,text=i[4])
            EL6 = Label(show,text=i[5])
            EL7 = Label(show,text=i[6])
            EL1.place(x=19,y=no + 68)
            EL2.place(x=120,y=no + 68)
            EL3.place(x=260,y=no + 68)
            EL4.place(x=320,y=no + 68)
            EL5.place(x=450,y=no + 68)
            EL6.place(x=550,y=no + 68)
            EL7.place(x=670,y=no + 68)

            TL = Label(show,text='----------------------------------------------------------------------------------------------------------------------------------------------------------')
            TL.place(x=10,y=no + 90)
            no += 40

        show.mainloop()                
        con.commit()

    def del_user():
        user = Tk()
        user.title('Remove User')
        user.geometry('400x100+550+300')

        def deleting():
            dele = E1.get()
            con = sql.connect('project.db')
            c = con.cursor()
            print(1)
            for i in c.execute('SELECT * FROM users'):
                print(i[5])
                if dele==i[5]:
                    print(3)
                    c.execute("DELETE FROM users WHERE username='" + dele + "'")
                    print(4)
            con.commit()
            con.close()
           

        L1 = Label(user, text='Enter username to be removed')
        E1 = Entry(user, bd=2)
        B = Button(user, text='Remove', width=13, command=deleting)
        L1.pack()
        E1.pack()
        B.pack()


    def db():
        con = sql.connect('project.db')
        c = con.cursor()

        show = Tk()
        show.title('All records')
        show.geometry("780x500+300+100")

        TL1 = Label(show,text='------------------------------------------------------------------------------------------------------------------------------------------------------')
        TL2 = Label(show,text='------------------------------------------------------------------------------------------------------------------------------------------------------')
        TL3 = Label(show,text='ID')
        TL4 = Label(show,text='Name')
        TL5 = Label(show,text='Author')
        TL6 = Label(show,text='Price')
        TL1.place(x=10,y=10)
        TL2.place(x=10,y=50)
        TL3.place(x=50,y=35)
        TL4.place(x=110,y=35)
        TL5.place(x=380,y=35)
        TL6.place(x=650,y=35)

        c.execute('CREATE TABLE IF NOT EXISTS books(Name, Author, Price)')
        no = 0
        for i in c.execute('SELECT * FROM books'):
            EL1 = Label(show,text=i[0])
            EL2 = Label(show,text=i[1])
            EL3 = Label(show,text=i[2])
            EL4 = Label(show,text=i[3])
            EL1.place(x=50,y=no + 68)
            EL2.place(x=110,y=no + 68)
            EL3.place(x=380,y=no + 68)
            EL4.place(x=650,y=no + 68)

            TL = Label(show,text='------------------------------------------------------------------------------------------------------------------------------------------------------')
            TL.place(x=10,y=no + 90)
            no += 40
        con.commit()


    def add():
        from book_record import submit
        submit()

    def remove():
        def check():
            dele = E1.get()
            con = sql.connect('project.db')
            c = con.cursor()
            print(1)
            for i in c.execute('SELECT * FROM books'):
                print(2)
                if dele==i[0]:
                    print(3)
                    c.execute("DELETE FROM books WHERE id=?",(i[0]))
                    print(4)
            con.commit()
            con.close()

        remove = Tk()
        remove.title('Removing book record')
        remove.geometry('400x100+500+200')

        L1 = Label(remove, text='Enter book ID to be removed')
        E1 = Entry(remove, bd=2)
        B = Button(remove, text='Remove', width=13, command=check)
        L1.pack()
        E1.pack()
        B.pack()

        remove.mainloop()

    def req():
        con = sql.connect('project.db')
        c = con.cursor()

        show = Tk()
        show.title('All requests')
        show.geometry("350x400+300+100")

        TL1 = Label(show,text='------------------------------------------------------------')
        TL2 = Label(show,text='------------------------------------------------------------')
        TL3 = Label(show,text='Name')
        TL4 = Label(show,text='Author')
        TL1.place(x=10,y=10)
        TL2.place(x=10,y=50)
        TL3.place(x=30,y=35)
        TL4.place(x=170,y=35)

        c.execute('CREATE TABLE IF NOT EXISTS books(Name, Author, Price)')
        no = 0
        for i in c.execute('SELECT * FROM req'):
            EL1 = Label(show,text=i[0])
            EL2 = Label(show,text=i[1])
            EL1.place(x=29,y=no + 68)
            EL2.place(x=169,y=no + 68)

            TL = Label(show,text='------------------------------------------------------------')
            TL.place(x=10,y=no + 90)
            no += 40
        con.commit()

    def ask():                                                              #prompt to ask while exiting main window
        a = messagebox.askokcancel("BMS","Are you sure to Logout?")
        if a==True:
            admin_log.destroy()

    def clear_req():
        con = sql.connect('project.db')
        c = con.cursor()
        c.execute("DROP TABLE if exists req")
        con.commit()
        con.close()

    L = Label(admin_log, text='Logged in as ADMIN', font=('Canberra',8,'bold'))
    B1 = Button(admin_log, width=20, text="See all users",bg='#FFFF99', command=users)
    B2 = Button(admin_log, width=20, text='Remove user', bg='#FFFF99',command=del_user)
    B3 = Button(admin_log, width=20, text="All books", bg='skyblue', command=db)
    B4 = Button(admin_log, width=20, text="Add new book", bg='skyblue', command=add)
    B5 = Button(admin_log, width=20, text="Remove a book", bg='skyblue', command=remove)
    B6 = Button(admin_log, width=20, text="Book requests", bg='skyblue', command=req)
    B7 = Button(admin_log, width=20, text="Clear requests", bg='skyblue',command=clear_req)
    B8 = Button(admin_log, width=15, text='Logout', bg='pink', command=ask)
    L.place(x=5,y=2)
    B1.place(x=135,y=50)
    B2.place(x=135,y=90)
    B3.place(x=135,y=130)
    B4.place(x=135,y=170)
    B5.place(x=135,y=210)
    B6.place(x=135,y=250)
    B7.place(x=135,y=290)
    B8.place(x=152,y=330)


    admin_log.mainloop()



#######################################################################################################
##                                                                                                   ##
##                                         local_log()                                               ## 
##                                                                                                   ##
#######################################################################################################


#    Functions inside local_log:
# req  -  Takes input for requested books and stores in table 'req' in database 'project.db'
# db   -  Fetches data from table 'books' from database and displays on screen.
# ask  -  prompts before exiting window.

def local_log():
    local_log = Tk()
    local_log.title('BMS')
    local_log.geometry("400x300+500+200")

    def req():
        req = Tk()
        req.title("Request")
        req.geometry('400x200+520+250')

        def check():
            name = E1.get()
            auth = E2.get()
            if len(E1.get())==0 or len(E2.get())==0:
                messagebox.showinfo('Violation','Entry cannot be empty')
            if len(E1.get())!=0 and len(E2.get())!=0:
                requesting()

        def requesting():
            name = E1.get()
            auth = E2.get()
            con = sql.connect('project.db')
            c = con.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS req(Name,Author)')
            c.execute('INSERT INTO req VALUES (?,?)',(name,auth))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Record added successfully to BMS')

        L = Label(req, text='Enter Book details', font=('Arial',13))
        L1 = Label(req, text='Name')
        L2 = Label(req, text='Author')
        E1 = Entry(req, width=35, bd=2)
        E2 = Entry(req, width=35, bd=2)
        B = Button(req, text='Request', bg='skyblue', width=13, command=check)
        L.pack()
        L1.pack()
        E1.pack()
        L2.pack()
        E2.pack()
        B.pack()

        req.mainloop()

    def db():
        con = sql.connect('project.db')
        c = con.cursor()

        show = Tk()
        show.title('All records')
        show.geometry("780x500+300+100")

        TL1 = Label(show,text='------------------------------------------------------------------------------------------------------------------------------------------------------')
        TL2 = Label(show,text='------------------------------------------------------------------------------------------------------------------------------------------------------')
        TL3 = Label(show,text='ID')
        TL4 = Label(show,text='Name')
        TL5 = Label(show,text='Author')
        TL6 = Label(show,text='Price')
        TL1.place(x=10,y=10)
        TL2.place(x=10,y=50)
        TL3.place(x=50,y=35)
        TL4.place(x=110,y=35)
        TL5.place(x=380,y=35)
        TL6.place(x=650,y=35)

        c.execute('CREATE TABLE IF NOT EXISTS books(Name, Author, Price)')
        no = 0
        for i in c.execute('SELECT * FROM books'):
            EL1 = Label(show,text=i[0])
            EL2 = Label(show,text=i[1])
            EL3 = Label(show,text=i[2])
            EL4 = Label(show,text=i[3])
            EL1.place(x=50,y=no + 68)
            EL2.place(x=110,y=no + 68)
            EL3.place(x=380,y=no + 68)
            EL4.place(x=650,y=no + 68)    

            TL = Label(show,text='------------------------------------------------------------------------------------------------------------------------------------------------------')
            TL.place(x=10,y=no + 90)
            no += 40
        con.commit()

    def ask():
        a = messagebox.askokcancel("BMS","Are you sure to Logout?")
        if a==True:
            local_log.destroy()

    L = Label(local_log, text='Logged in as Local User', font=('Canberra',8,'bold'))
    B1 = Button(local_log, width=14, bg='skyblue', text="See all books",command=db)
    B2 = Button(local_log, width=14, bg='skyblue', text="Request a book", command=req)
    B3 = Button(local_log, width=14, bg='skyblue', text='Logout',command=ask)
    L.place(x=5,y=2)
    B1.place(x=145,y=50)
    B2.place(x=145,y=100)
    B3.place(x=145,y=150)

    local_log.mainloop()

#local_log()
#a_log()