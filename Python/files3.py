#   dosyanın başına veri ekleme
with open("dosya.txt","r+") as dosya:
    data = dosya.read()
    dosya.seek(0)
    data = "Merhaba\n" + data
    dosya.write(data)



