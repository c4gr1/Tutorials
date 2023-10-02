a = 50
b = 40
toplam = a + b

if(toplam > 100):
    print("toplamlar 100den buyuk\n")
else:
    print("toplamlar 100den kucuk\n")

################################################  

yas = int(input("yaşını gir : "))

if(yas>17):
    print("ehliyet alabilirsin")
else:
    print("ehliyet alamazsın")

################################################

not1 = int(input("\n1. not : "))
not2 = int(input("2. not : "))

ort = (not1+not2)/2

if(not1<30 or not2<30):
    print("NA cominggggg")

if(ort>49.9 and ort<100):
    print("dersi geçtin")
    print("not ortalaman ...",ort)
elif(ort==100):
    print("seneye gel sen anlat")
else:
    print("kaldın babacımmm")
    print("not ortalaman ...",ort)

################################################

for sayac in range(10):
    print (sayac+1,"cagrii")

################################################

a = 0;

while(a<5):
    print("while looop")
    a+=1

# a=a+1 ile a+=1 aynı şey a++ kabul edilmiyor

#while True sonsuz döngü yapar

stop=0

while True:
    
    sayi1 = int(input("1. sayiyi giriniz: "))
    sayi2 = int(input("2. sayiyi giriniz: "))
 
    toplam = sayi1+sayi2
    
    print("toplam =",toplam)

    stop = stop + 1

    if(stop==1):
        print("")
        break

################################################

words = ['a', 'ab', 'abi']
for w in words:
    print(w, len(w))

################################################

a = ['cagri', 'is', 'trying', 'to', 'learn','python']
for i in range(len(a)):
    print(i, a[i])    






