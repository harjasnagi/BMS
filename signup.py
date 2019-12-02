from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image

#signup() function creates the window 'sign' where signup details for entered.
def signup():
    
    sign = Tk()
    sign.title('Sign up BMS')
    sign.geometry("400x490+500+100")
    sign.configure(bg='#DDDD88')

#check() function checks for empty entries. It also checks if the password and retype password match or not.
    def check():
        if len(E1.get())==0:
            messagebox.showinfo('Violation','Name cannot be empty')
        elif len(E2.get())==0:
            messagebox.showinfo('Violation','Email cannot be empty')
        elif len(E4.get())==0:
            messagebox.showinfo('Violation','Mobile number cannot be empty')
        elif len(E4.get())<10:
            messagebox.showinfo('Violation','Invalid Mobile number')
        elif len(E5.get())==0:
            messagebox.showinfo('Violation','Address cannot be empty')
        elif len(E6.get())==0:
            messagebox.showinfo('Violation','Username cannot be empty')
        elif len(E7.get())==0:
            messagebox.showinfo('Violation','Password cannot be empty')
        elif (E7.get())!=(E8.get()):
            messagebox.showinfo('Violation','Passwords donot match')
        else:
            write()

#write() function uploads the entered data from check() function to sql database table.
    def write():
        import sqlite3 as sql
        name = E1.get()
        email = E2.get()
        z = v.get()
        if z==0:
            gen='M'
        elif z==1:
            gen='F'
            
        number = E4.get()
        addr = E5.get()
        uname = E6.get()
        passw = E7.get()
        
        conn = sql.connect('project.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS users(Name,Email,Gender,Mobile,Address,Username,Password)')
        c.execute('INSERT INTO users VALUES (?,?,?,?,?,?,?)',(name,email,gen,number,addr,uname,passw))
        conn.commit()
        messagebox.showinfo('Success','Record added successfully to BMS')


    L1 = Label(sign, text="Name", bg='#DDDD88')
    L2 = Label(sign, text="Email", bg='#DDDD88')
    L3 = Label(sign, text="Gender", bg='#DDDD88')
    L4 = Label(sign, text="Mobile no.", bg='#DDDD88')
    L5 = Label(sign, text="Address", bg='#DDDD88')
    L6 = Label(sign, text='Username', bg='#DDDD88')
    L7 = Label(sign, text='Password', bg='#DDDD88')
    L8 = Label(sign, text='Retype Password', bg='#DDDD88')

    E1 = Entry(sign, bd=2)
    E2 = Entry(sign, bd=2)
    E4 = Entry(sign, bd=2)
    E5 = Entry(sign, bd=2)
    E6 = Entry(sign, bd=2)
    E7 = Entry(sign, bd=2, show='*')
    E8 = Entry(sign, bd=2, show='*')

    v=IntVar()
    R1 = Radiobutton( sign, text="M", variable=v, value=0, bg='#DDDD88')
    R2 = Radiobutton( sign, text="F", variable=v, value=1, bg='#DDDD88')
    B1 = Button(sign, text="SIGN UP", width=12, bg='skyblue', font=('Comic Sans MS',8), command=check)
    B2 = Button(sign, text='CANCEL', width=12, bg='pink', font=('Comic Sans MS',8), command =sign.destroy)
    
    L1.place(x=65,y=30)
    E1.place(x=170,y=30)
    
    L2.place(x=65,y=80)
    E2.place(x=170,y=80)
    
    L3.place(x=65,y=130)
    R1.place(x=170,y=130)
    R2.place(x=210,y=130)
    #E3.place(x=150,y=130)
    
    L4.place(x=65,y=180)
    E4.place(x=170,y=180)

    L5.place(x=65,y=230)
    E5.place(x=170,y=230)

    L6.place(x=65,y=280)
    E6.place(x=170,y=280)

    L7.place(x=65,y=330)
    E7.place(x=170,y=330)

    L8.place(x=65,y=380)
    E8.place(x=170,y=380)

    B1.place(x=110,y=425)
    B2.place(x=230,y=425)
    
    sign.mainloop()
    
#signup()
