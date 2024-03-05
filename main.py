from tkinter import *
import pandas as pd 
from tkinter import messagebox
import numpy as np

root = Tk()
root.attributes("-fullscreen" , True )
root.config(bg= "#000000")



    
def homePage():
    pass

def logSystem():
    name = LGentry_user.get()
    password = LGentry_pass.get()
    name_location = -1
    pass_location = -1

    with open("log.txt", "r") as file:
        login_data = file.readlines()

    for index, value in enumerate(login_data):
        if name == value.strip():  
            name_location = index
            break   

    for index, value in enumerate(login_data):
        if password == value.strip():
            pass_location = index
            break

    if name == "":
        messagebox.showerror("Error", "Enter username")
    elif name_location == -1:  
        messagebox.showerror("Error", "Your name is not in the system")
    elif password == "":
        messagebox.showerror("Error", "Enter password")
    elif pass_location == -1:  
        messagebox.showerror("Error", "Invalid password")
    elif pass_location != name_location + 1:
        messagebox.showerror("Error", "Password and username don't match")
    else:
        homePage()
        LGframe.destroy()

def Login () :
    global LGframe
    global LGentry_pass
    global LGentry_user
    
    CAframe.destroy()
    LGframe = Frame(root, relief="solid", bg="#171717")
    LGframe.pack(expand=True)

    LGlabel_title = Label(LGframe, text='LOGIN', bg="#171717", fg="#ffffff")
    LGlabel_user = Label(LGframe, text="Username", font=('Open Sans', 12), bg="#171717", fg="#ffffff" )
    LGlabel_pass = Label(LGframe, text="Password", font=('Open Sans', 12), bg="#171717", fg="#ffffff")
    LGentry_user = Entry(LGframe, font=('Open Sans', 14))
    LGentry_pass = Entry(LGframe, show='*', font=('Open Sans', 14))
    LGbutton_login = Button(LGframe, text="LOGIN", command=logSystem)
    LGlabel_go_to_singup =  Checkbutton(LGframe, text="I DO NOT HAVE AN ACCOUNT", font=('Open Sans', 10), bg="#171717", fg="#ffffff" , command= goSingUP )

    LGlabel_title.pack()
    LGlabel_user.pack(padx=10, pady=5)
    LGentry_user.pack(padx=10, pady=5)
    LGlabel_pass.pack(padx=10, pady=5)
    LGentry_pass.pack(padx=10, pady=5)
    LGbutton_login.pack(pady= 5)
    LGlabel_go_to_singup.pack( pady=5)

def singup () :
    global CAframe
    global CAentry_user
    global CAentry_pass
    
    
    CAframe = Frame(root, relief="solid", bg="#171717")
    CAframe.pack(expand=True)

    CAlabel_title = Label(CAframe, text='create account', bg="#171717", fg="#ffffff")
    CAlabel_logl =  Checkbutton(CAframe, text="alredy singup", font=('Open Sans', 12), bg="#171717", fg="#ffffff" , command= Login ) 
    CAlabel_user = Label(CAframe, text="Create Username", font=('Open Sans', 12), bg="#171717", fg="#ffffff" )
    CAlabel_pass = Label(CAframe, text="Create Password", font=('Open Sans', 12), bg="#171717", fg="#ffffff")
    CAentry_user = Entry(CAframe, font=('Open Sans', 14))
    CAentry_pass = Entry(CAframe, show='*', font=('Open Sans', 14))
    CAbutton_singup = Button(CAframe, text="Sign up", command=toLogin)

    CAlabel_title.pack()
    CAlabel_user.pack(padx=10, pady=5)
    CAentry_user.pack(padx=10, pady=5)
    CAlabel_pass.pack(padx=10, pady=5)
    CAentry_pass.pack(padx=10, pady=5)
    CAbutton_singup.pack(pady= 5)
    CAlabel_logl.pack(pady = 5) 

def goSingUP ():
    LGframe.destroy()
    singup()

def toLogin():
    global login_data
    login_data = []
    
    name = CAentry_user.get()
    password = CAentry_pass.get()
    with open("log.txt" , "a" ) as file :
        test_name =file.read(login_data[0])
        test_pass =file.read(login_data[1])
        
    if name != "":
        login_data.append(name)
    else:
        messagebox.showerror("Error", " Nzalo does not like you ")
    if password == "":
        messagebox.showerror("Error", "enter password ")
    elif len(password) <= 6:
        messagebox.showerror("Error", "password must be at least 6 characters")
    else:
        login_data.append(password)
        CAframe.destroy()
        Login ()
