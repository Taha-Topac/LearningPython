def kontrol(str):
      sayac = 0
      sonuc = False
      for ch in str:
            if ch.replace("g","G"):
                  sayac = sayac + 1
                  sonuc = True
                  break
      return sonuc
 
metin=input('Metin : ')
print(kontrol(metin))
if(kontrol(metin)==True):
      print('g karakteri metin içinde var')
else:
      print('g karakteri metin içinde yok')