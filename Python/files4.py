#  istenilen yere veri ekleme
with open("dosya.txt","r+") as dosya:
    data = dosya.readlines()
    data.insert(1,"deneme\n")
    dosya.seek(0)
    dosya.writelines(data)
