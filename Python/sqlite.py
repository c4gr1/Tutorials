import sqlite3

con = sqlite3.connect("dersler.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT,soyad TEXT,numara INT)")
    con.commit()

def deger_ekle():
        cursor.execute("INSERT INTO ogrenciler VALUES('Erol','Yildiz',28)")
        con.commit()
        con.close()

tablo_olustur()
deger_ekle()