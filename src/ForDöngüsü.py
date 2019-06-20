a=int(input("Sayıyı gir: "))
ç=0
t=0

for x in range(a):
    if x % 2==0:
        print(x,"= çift sayı")
        ç+=x
    else:
        print(x,"=tek")
        t+=x
print("----------------------------")
print("tek sayıların toplamı={0}".format(t))
print("----------------------------")
print("çift sayıalrın toplamı={0}".format(ç))
      