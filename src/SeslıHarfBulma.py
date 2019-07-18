sesliharfler = 'aeıioöuü'
 
a = input("Bir yazı giriniz = ")
 
a = a.casefold() 

number = {}.fromkeys(sesliharfler,0)
 
for harf in a:
   if harf in number:
       number[harf] = number[harf] + 1
print(number)