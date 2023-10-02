import random

num = random.randint(0,100)
kalanTahmin=5
for i in range(5):
    tahmin = int(input("tahmin yap(0-100) :"))
    if(num == tahmin) :
        print("bildin")
        break

    else:
        kalanTahmin-=1
        if(kalanTahmin!=0):
            print("kalan hakkin",kalanTahmin)
            if(tahmin > num):
                print("sayi daha kucuk olmalı")
            else:
                print("sayi daha buyuk olmalı")

        else:
            print("hakkin bitti go")
            
print("sayi",num,"idi")
