
from tkinter import *
from tkinter import messagebox

def Çarpma():
    e1=giris1.get()
    e2=giris2.get()

    sonuc=float(e1)*float(e2)
    var=messagebox.showinfo("Sonuç","Cevap={0}".format(sonuc))

def Çıkarma():
    e1=giris1.get()
    e2=giris2.get()

    sonuc=float(e1)-float(e2)
    var=messagebox.showinfo("Sonuç","Cevap={0}".format(sonuc))

def yeni():         
    global Etext    
    Etext=""
    Eyazi.set(Etext)
    global Itext
    Itext=""
    Iyazi.set(Itext)
    pencere.config(text="Yeni hesap için hazır", font=("bold", 12), fg="white", bd=2)
def Bölmeİşlemi():
    e1=giris1.get()
    e2=giris2.get()
    sonuc=float(e1)/float(2)
    var=messagebox.showinfo("Sonuç","Vevaplar={0}".format(sonuc))
def hesapla():
    
    Eyazi=giris1.get() 
    Iyazi=giris2.get()
    sonuç=float(Eyazi)+float(Iyazi)
    var=messagebox.showinfo("sonuç","cevap={0}".format(sonuç))

pencere = Tk()

pencere.title=("Taha Topaç")
pencere.geometry("400x400")
pencere.config(bg="#004040")

Eyazi=StringVar() 
Iyazi=StringVar()
Etext=""
Itext=""
Label(text="1.Sayıyı Girin ",bg="#004040").place(x=50,y=33)
giris1=Entry()
giris1.config(textvariable=Eyazi, bg="white")
giris1.place(x=50,y=60)

Label(text="2.Sayıyı Girin",bg="#004040").place(x=50,y=80)
giris2=Entry()
giris2.config(textvariable=Iyazi, bg="white")
giris2.place(x=50,y=100)
 

Button(text="Topla", command=hesapla, font=("bold", 12)).place(x=75, y=150, width=70, height=35)
Button(text="Bölme", command=Bölmeİşlemi, font=("bold", 12)).place(x=75, y=200, width=70, height=35)
Button(text="Çarpma", command=Çarpma, font=("bold", 12)).place(x=75, y=250, width=70, height=35)
Button(text="Çıkarma", command=Çıkarma, font=("bold", 12)).place(x=75, y=300, width=70, height=35)
Button(text="Temizle", command=yeni,font=("bold,",12)).place(x=75,y=350,width=70, height=35) 
pencere.mainloop()
