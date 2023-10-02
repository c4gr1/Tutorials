import sqlite3
import random
import time
import datetime

con = sqlite3.connect("sql_tablo.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1(isim TEXT,zaman REAL,tarih TEXT,key TEXT,deger REAL)")

def rastgele_deger_ekle(ad):
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    key = "cagri"
    deger = random.randrange(0,10)
    cursor.execute("INSERT INTO Tablo1 (isim,zaman,tarih,key,deger) VALUES(?,?,?,?,?)",(ad,zaman,tarih,key,deger))
    con.commit()

def tablodan_oku():
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print(type(data))
    for i in data:
        print(i)

def tablo_guncelle():
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("Öncesiiiiiiiii")
    for i in data:
        print(i)

    cursor.execute("DELETE FROM Tablo1 Where deger = 2")
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("deleteden sonra")
    for i in data:
        print(i)
#aşağıdaki kodun db dosyasını değiştirmeini istiosan oraya da con.commit yaz
    con.commit()
"""        
    cursor.execute("UPDATE Tablo1 SET deger = 99 WHERE deger = 0.0")
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    print("sonrasiiiiiiii")
    for i in data:
        print(i) 
"""



tablo_olustur()
tablodan_oku()
#tablo_guncelle()

i=10
for i in range(3):
    ad=input("your name:")
    rastgele_deger_ekle(ad)
    time.sleep(1)

con.close()