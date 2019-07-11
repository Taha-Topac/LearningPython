import sqlite3

con=sqlite3.connect("Kişiler.db")

cursor=con.cursor()


def tablaolustur():
    cursor.execute("CREATE TABLE Kişiler(ad text,soyad text,şifre int)")
    con.commit()
    con.close()

tablaolustur()