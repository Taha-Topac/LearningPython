from tkinter import *
from tkinter import messagebox
import sys


def yeni():         # kutulari temizlemek icin
    global Etext    # global, Etext degiskenini tum programda kullanilabilir yapiyor
    Etext=""
    Eyazi.set(Etext)
    global Itext
    Itext=""
    Iyazi.set(Itext)
    global Rtext
    Rtext=""
    Ryazi.set(Rtext)
    ekran.config(text="Yeni hesap için hazır", font=("bold", 12), bg="#004040", fg="white", bd=2)

def formuller():
    ekran.config(text="Formüller: E=I*R  I=E/R  R=E/I", font=("bold", 12), bg="#004040", fg="white", bd=2)

def hesapla():
    try: # sayi girilmisse (hata incelemesi yapiliyor, hata yoksa)
        EEE=Egiris.get() # kutulardaki bilgiler çagriliyor
        III=Igiris.get()
        RRR=Rgiris.get()
        if EEE!="" and III!="" and RRR!="":
            ekran.config(text="Bütün kutular dolu, bilinmeyeni boşaltınız", font=("bold", 10), bg="red", fg="white", bd=2)
			#sonuc ekran etiketine (Label) yazildi			
        elif EEE=="" and III=="" and RRR=="":
            ekran.config(text="Bütün kutular boş, bilinenleri doldurunuz", font=("bold", 10), bg="red", fg="white", bd=2)
        elif (EEE=="" and III=="" and RRR!="") or (EEE!="" and III=="" and RRR=="") or (III!="" and EEE=="" and RRR==""):
            ekran.config(text="Dikkat! Kutuların biri boş, ikisi dolu olmalıdır", font=("bold", 10), bg="red", fg="white", bd=2)
        elif EEE!="" and III!="" and RRR=="":
            RR=float(EEE)/float(III) #Ondalik sayi girilebilmesi icin float() kullanildi
            ekran.config(text="R="+str(RR), font=("bold", 18), bg="#004040", fg="red", bd=2)        
        elif EEE!="" and III=="" and RRR!="":
            II=float(EEE)/float(RRR)
            ekran.config(text="I="+str(II), font=("bold", 18), bg="#004040", fg="red", bd=2)
        elif EEE=="" and III!="" and RRR!="":
            EE=float(III)*float(RRR)
            ekran.config(text="E="+str(EE), font=("bold", 18), bg="#004040", fg="red", bd=2)        
    except: #sayi disinda karakter girilmis ve islem yapılamıyorsa
            ekran.config(text="Sadece sayı giriniz!")
            
def hakkinda():
    ekran.config(text="Hazırlayan: Taha TOPAÇ ", font=("normal", 10), bg="#004040", fg="white", bd=2)
    
def yardim():
    ekran.config(text="Yardım için:https://github.com/Taha-Topac bakabilrisiniz", font=("normal", 10), bg="#004040", fg="white", bd=2)


pencere=Tk()
pencere.title("Ohm Kanunu Değer Hesaplayıcı") # pencere basligi
pencere.geometry("450x200") # pencere boyutlari

Eyazi=StringVar() # global degiskenler icin
Iyazi=StringVar()
Ryazi=StringVar()
Etext=""
Itext=""
Rtext=""
# bilgilendirme amacli ekrani cagirma dugmeleri
Button(text="Formüller", command=formuller, font=("bold", 10)).place(x=365, y=12, width=80, height=35)
Button(text="Hakkında", command=hakkinda, font=("bold", 10)).place(x=365, y=50, width=80, height=35)
Button(text="Yardım", command=yardim, font=("bold", 10)).place(x=365, y=90, width=80, height=35)
# Gerilim Girisi
Label(text="E=", font=("bold", 12)).place(x=10,y=60)
Egiris=Entry()
Egiris.config(textvariable=Eyazi, bg="white")
Egiris.place(x=40,y=60,width=50)
Label(text="Volt E=I*R", font=("normal", 10)).place(x=90,y=60)
# Akim girisi
Label(text="I=", font=("bold", 12)).place(x=10,y=90)
Igiris=Entry()
Igiris.config(textvariable=Iyazi, bg="white")
Igiris.place(x=40,y=90,width=50)
Label(text="Amper I=E/R", font=("normal", 10)).place(x=90,y=90)
# Direnc girisi
Label(text="R=", font=("bold", 12)).place(x=10,y=120)
Rgiris=Entry()
Rgiris.config(textvariable=Ryazi, bg="white")
Rgiris.place(x=40,y=120,width=50)
Label(text="Ohm R=E/I", font=("normal", 10)).place(x=90,y=120)
# Ekran (islem sonuclarinin ve uyarılarin kullaniciya aktarildigi alan)
ekran=Label()
ekran.config(text="Yeni hesap için hazır", font=("bold", 12), bg="#004040", fg="white", bd=2)
ekran.place(x=10,y=10,width=350,height=40)
# islem yapma amacli dügmeler
Button(text="Hesapla", command=hesapla, font=("bold", 16), bg="#E1F2F7").place(x=10, y=150, width=260, height=35)
Button(text="Yeni", command=yeni, font=("bold", 12), bg="#E1F2F7").place(x=280, y=150, width=50, height=35)
Button(text="Çıkış", command=sys.exit, font=("bold", 12), bg="#FFCCFF").place(x=395, y=150, width=50, height=35)

pencere.mainloop()