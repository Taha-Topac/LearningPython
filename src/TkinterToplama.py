from tkinter import *
from tkinter import messagebox


pencere = Tk()

pencere.title=("Taha Topaç")
pencere.geometry("400x300")

giris1=Entry()
giris1.config(textvariable=giris1, bg="white")
giris1.place(x=50,y=50)

giris2=Entry()
giris2.config(textvariable=giris2, bg="white")
giris2.place(x=50,y=100)

btn=Button
pencere.mainloop()
