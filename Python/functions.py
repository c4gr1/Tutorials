def fact(num):
    faktöriyel =1
    for i in range(1,num+1):
        faktöriyel*=i

    return faktöriyel

sayi = int(input("sayi :"))

a = fact(sayi)

print(a)

def kokBul(a,b,c):
    delta = (b*b-4*a*c)
    if(delta<0):
        print("reel kok yok")
        return
    
    x1=(-b-delta**0.5)/2*a
    x2=(-b+delta**0.5)/2*a

    return(x1,x2)

print("katsayilar pls")
katsayi1 = int(input("a :"))
katsayi2 = int(input("b :"))
katsayi3 = int(input("c :"))

sonuc = kokBul(katsayi1,katsayi2,katsayi3)

if(sonuc):
    print(sonuc)

def deneme(array):
    if(array[0]==0 and array[1]==0):
        print("0")
    
    elif(array[0]==1 and array[1]==0):
        print("1")
    
    elif(array[1]==0 and array[0]==1):
        print("1")

    elif(array[1]==1 and array[0]==1 ):
        print("1")

    else:
        print("404 not found")
    

deneme(['a',0])
