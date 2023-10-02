#dosya okuma metodları
dosya = open("dosya.txt","r")

#print(dosya.readlines())

liste = dosya.readlines()

print(liste[1])

#print(dosya.readline())
#print(dosya.readline())
#print(dosya.readline())

# print(dosya.read())

#read()
#readline()
#readlines()

dosya.close()