#   büyük dosyalarda bunu kullanmak daha iyi,imleç hareket ettirme
with open("dosya.txt","r") as dosya:
    dosya.seek(5)
    isim = dosya.read(5)
    print("isim :",isim)