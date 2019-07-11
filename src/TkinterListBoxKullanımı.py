from tkinter import *
from tkinter import messagebox
 
pencere = Tk()
 
pencere.title=("Taha Topaç")
pencere.geometry("400x300")
 
uygulama = Frame(pencere)
mystring = StringVar()
uygulama.grid()
 

Lb1 = Listbox(uygulama,width=20,height=4)
Lb1.insert(1, "Python")
Lb1.insert(2, "C#")
Lb1.grid(padx=110, pady=10)

def yazı():
    var=messagebox.showinfo("Bilgi", "Kaydedildi")

button1=Button(uygulama, text= "Onayla" , width=15 , height=3 , command=yazı)
button1.grid(padx=100,pady=10)
 
pencere.mainloop()