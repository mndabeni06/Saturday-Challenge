from tkinter import *
master = Tk()
master.geometry('600x400')
master.config(bg='skyblue')
master.title('Second Screen')
# Calculating Age
age = Label(master, text='Please Enter Your Age:', borderwidth=5)
age.place(x=10, y=10)
age_entry = Entry(master, borderwidth=5)
age_entry.place(x=200, y=10)
from datetime import date, timedelta
dob = date(1999, 1, 20)
age = (date.today() - dob)//timedelta(days=365.245)
def age():
    age = ['16']
    for x in range(len(age)):
         if age_entry.get() == age[x]



master.mainloop()
