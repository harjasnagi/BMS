from tkinter import messagebox, filedialog
from tkinter import *
import sqlite3 as sql
from PIL import ImageTk, Image

main = Tk()
main.geometry("500x300+450+200")
main.title("Welcome to BMS (K18HK)")
main.resizable(width=False, height=False)

photo = PhotoImage(file = "tex2.png")									#the three lines set the background of 'main' window.
w = Label(main, image=photo)
w.pack()


def log():                                                              #redirects to login window file.
    from login import login
    login()

def sign():                                                             #redirects to signup window file.
    from signup import signup
    signup()

def ask():                                                              #prompts to ask while exiting main window.
    a = messagebox.askokcancel("BMS","Exit BMS application?")
    if a==True:
        main.destroy()

def books():                                                            #redirects to available books window file.
    pass
        
x="LOGOO.png"
img = Image.open(x)
img = img.resize((190, 190), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(main, image=img)
panel.image = img
panel.place(x=260,y=40)

L1 = Label(main, text='Welcome To BMS', font=('Comic Sans MS',14))
B1 = Button(main, text='LOGIN', width=10, bg='#66CCFF', command =log)
B2 = Button(main, text='SIGNUP', width=10,bg='#00FF99', command =sign)
B3 = Button(main, text='EXIT', width=10, bg='pink', command =ask)

L1.place(x=70,y=35)
B1.place(x=120,y=100)
B2.place(x=120,y=140)
B3.place(x=120, y=180)

main.mainloop()
