import datetime

now = datetime.datetime.now()
person = input("Adınızı giriniz > ")
print("Merhaba %s. Şu anda saat %s" % (person,now))