isimListesi = ["aaa","bbb","ccc","ddd"]
yillar = [1999,1969,1976,2002]

print(isimListesi)

for i in range(len(isimListesi)):
    print(isimListesi[i]) 

print("listede",len(isimListesi),"tane isim var")

index = yillar.index(1999)
print(f"aranan yil {index}. indexte")
deneme = f"aranan yil {index}. indexte"
print(deneme)

"""
yorum satırı böyle yapılıyor
"""

# append listenin sonunda yeni eleman ekler
isimListesi.append("öykü")

print(isimListesi)

# extend 2 listeyi birleştirir 
isimListesi.extend(yillar)

print(isimListesi)

# insert belirlenen indexe eleman ekler
isimListesi.insert(0,"ilkEleman")

print(isimListesi)

# delete verilen girdiyi siler
isimListesi.remove("öykü")

print(isimListesi)

# count listede kaç tane var onu bulur
found = isimListesi.count("cagri")
print("cagri",found,"kere var listede")

# pop girilen indexteki değeri siler
isimListesi.pop(0)
print(isimListesi)

yillar.sort()
print(yillar)

# isimListesi.sort() böyle kullanmak hata veriyor str ve int olduğu için
numbers = sorted([x for x in isimListesi if isinstance(x, int)])
strings = sorted([x for x in isimListesi if isinstance(x, str)])

isimListesi = numbers + strings

print(isimListesi)

# reverse listeyi tersine çeviri
isimListesi.reverse()

print(isimListesi)

# copy listenin shallow kopyasını oluşturur
copy = isimListesi.copy()

print(copy)

# clear listeyi temizler
isimListesi.clear()

print(isimListesi)

