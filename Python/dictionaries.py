sozluk = {"python":"meta dil","php":"script dili","java":"baba dil"}

print(type(sozluk)) 

print(sozluk["python"])

for i in sozluk.items():
    print(i)

for i in sozluk.items():
    print(i[0]+ "-" + i[1])

for i,j in sozluk.items():
    print(i + " " + j)

dersler = {"Ahmet":["Veri","Os"],"Ziya":["Java","Oop","C++"]}

isim = input("isim gir :")

print("{}in aldığı dersler:".format(isim))

for i in (dersler[isim]):
    print(i)
