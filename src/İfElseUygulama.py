from getpass import getpass

Ad="Taha"
Şifre=123456

ad1=input("Kullanıcı adınızı girin: ")
şifre=int(getpass('Şifre:'))

tekrarla = True

while tekrarla == True:
    if(Ad==ad1) and (Şifre==şifre):
        print("GİRİŞ BAŞARILI")
        print("---------------------")
        print("Hoş geldiniz:"+ad1 )
        print("Lütfen İşleminiz seçin")
        print("-1. Kullanıcı kayıt")
        print("-2. Kayıtlı olan kişiler")
        print("-3. Matamatiksel işlemler yap")
        print("---------------------")
        a1=int(input("Yapmak istediğiniz İşlemi tuşlayın:"))
        if(a1==1):
            kad=input("Yeni kayıt adını girin: ")
            kşifre=int(input("Yeni kayıt şifresini girin: "))
            print("Kullanıcı adı:%s   Şifre:%s "%(kad,kşifre))
            tekrarla = int(input("Tekrarlamak için 1'e basın >"))
            if tekrarla != 1:
                break
            else:
                continue
        if(a1==2):
            print("ASŞDASJ")
            tekrarla = int(input("Tekrarlamak için 1'e basın >"))
            if tekrarla != 1:
                break
            else:
                continue
        if(a1==3):
            print("---------------------")
            print("İşlem seçin")
            print("-1 Çarpma")
            print("-2 Bölme ")
            print("-3 Toplama")
            print("-4 Çıkarma")
            print("---------------------")
            a2=int(input("İşlemi seçin: "))
            if(a2==1):
                çsayı1 = input('1. Sayı : ')
                çsayı2= input('2. Sayı : ')
                çsonuç=float(çsayı1)*float(çsayı2)
                print("Sonuç :{0} ".format(çsonuç))
                tekrarla = int(input("Tekrarlamak için 1'e basın >"))
                if tekrarla != 1:
                    break
                else:
                    continue
            if(a2==2):
                bsayı1 = input('1. Sayı : ')
                bsayı3 = input('2. Sayı : ')
                bsonuç=float(bsayı1)/float(bsayı3)
                print("Sonuç :{0} ".format(bsonuç))
                tekrarla = int(input("Tekrarlamak için 1'e basın >"))
                if tekrarla != 1:
                    break
                else:
                    continue
            if(a2==3):
                tsayı1= input('1. Sayı : ')
                tsayı2= input('2. Sayı : ')
                tsonuç=float(tsayı1)+float(tsayı2)
                print("Sonuç :{0} ".format(tsonuç))
                tekrarla = int(input("Tekrarlamak için 1'e basın >"))
                if tekrarla != 1:
                    break
                else:
                    continue
            if(a2==4):
                csayı1 = input('1. Sayı : ')
                csayı2 = input('2. Sayı : ')
                csonuç=float(csayı1)-float(csayı2)
                print("Sonuç :{0} ".format(csonuç))
                tekrarla = int(input("Tekrarlamak için 1'e basın >"))
                if tekrarla != 1:
                    break
                else:
                    continue
            else:
                print("1-3 arası sayı girmediniz")   
                tekrarla = int(input("Tekrarlamak için 1'e basın >"))
            if tekrarla != 1:
                break
            else:
                continue        
        elif(a1<=0) and (a1>=4) :
            print("1-3 sayı girmediniz !!!!!")
    else:
        print("Giriş bilgileri yanlış")
    shouldExit = input("Çıkımak için q'ya da geri dönmek inin g ye basın > ")
    if shouldExit == "q":
        break
   
exit()

        


