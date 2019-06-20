from random import randint
 
rand=randint(1, 50)
sayac=0
 
while True:
    sayac+=1
    print("------------------------------------------")
    sayi=int(input("1 ile 50 arasında değer girin :"))
    if(sayi==0):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))