a1="taha"
a2=159753

a3=input("Adınızı girin:")
a4=input("Şifrenizi şifrenizi")

if ( a1==a3) and (a2==a4):
    print("Giriş başarılı !!! ")
elif ( a1!=a3) and (a2==a4):
    print("Kullamıcı adı yanlış !!! ")
elif ( a1==a3) and (a2!=a4):
    print("Şifre hatalı !!!! ")
else:
    print("Tekrar deneyin !!! ")


