from tkinter import *
root = Tk()
root.geometry('600x500')
root.title('Login_Form')
root.config(bg='red')
# Creating Widgets
username = Label(root, text="Please Enter Your Username:")
username.place(x=20, y=10)
username_entry = Entry(root, borderwidth=5)
username_entry.place(x=300, y=10)
password = Label(root, text='Please Enter Your Password:')
password.place(x=20, y=50 )
password_entry = Entry(root, borderwidth=5,  show="*")
password_entry.place(x=300, y=50)

# Defining Functions

def login():
     # importing message box
    from tkinter import messagebox
    Username = ["Karabo", "Masimthembe", "Malik", "Jardien", "Likho"]
    Password = ["123", "456", "789", "101", "131"]
    # boolean variable
    found = False
    for x in range(len(Username)):
        if username_entry.get()==Username[x] and password_entry.get()==Password[x]:
            found=True
    if found==True:
        messagebox.showinfo("PERMISSION", "Access Granted")
        root.destroy()
        import Second_Screen
    else:
        messagebox.showinfo("ERROR INFO", "Access Denied")


def logout():
    username_entry.delete(0,END)
    password_entry.delete(0, END)

def clear():
    username_entry.delete(0, END)
    password_entry(0, END)



login_btn = Button(root, text='Login', borderwidth=5, command=login)
login_btn.place(x=20, y=100)
logout_btn = Button(root, text='Logout', borderwidth=5, command=logout)
logout_btn.place(x=200, y=100)
clear_btn = Button(root, text='Clear', borderwidth=5,command=clear)
clear_btn.place(x=400, y=100)

root.mainloop()
