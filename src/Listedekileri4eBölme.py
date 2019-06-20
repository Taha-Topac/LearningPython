 
sayilar = [18,22,15,85,65,30,10,20,32,34,28,101,5,4,32,55,40,38,34,36,30,32,86,80,92]
sayac=0 
for sayi in sayilar:
   if sayi%4 == 0:
      print (str(sayi)+ (" : 4'in katıdır."))
      sayac=sayac+1
else:
   print ('Döngü Bitti')
print("4'in katı olan sayı adeti : "+str(sayac))
 
