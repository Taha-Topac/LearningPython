vize = input('Vize Notunuz : ')
final = input('Final Notunuz : ')
ortalama=(float(vize)*0.3)+(float(final)*0.7)
print("Ortalama :{0} ".format(ortalama))

if ortalama <=50:
    print("Kaldınız")
else:
    print("Geçtiniz")