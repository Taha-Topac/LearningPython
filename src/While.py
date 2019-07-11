a1=1
a5=0
a4=0

a2=int(input("Lütfen sayınızı girin:"))

while int(a1)<int(a2):
    a3=a1%2
    if (a3==1):
        print("Sayınız tek:"+a1)
        a4=a1+a4
        a1=a1+1
    else:
        print("sayunuz çift:"+a1)
        a5=a1+a5
        a1=a1+1

