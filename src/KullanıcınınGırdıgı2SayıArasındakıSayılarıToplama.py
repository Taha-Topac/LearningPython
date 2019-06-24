a1=int(input("1. Sayıyı girin: "))
a2=int(input("2. Sayıyı girin: "))

a3=0

for i in range(int(a1)+1,int(a2)):
    a3+=i  
    print("Sayılar: %s "%(i))
print("Cevap: %s"%(a3))