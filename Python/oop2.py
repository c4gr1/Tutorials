import random

class Dusman:  
    def __init__(self,ad="Dusman",kc=100,sg=10,ms=1):
        self.isim = ad
        self.kalan_can = kc
        self.saldırı_gucu = sg
        self.mermi_sayisi = ms

    def print(self):
        print("İsim:",self.isim,"Kalan Can:",self.kalan_can,"Saldırı Gücü:",self.saldırı_gucu,"Mermi Sayisi:",self.mermi_sayisi)

    def saldir(self):
        print(self.isim + " saldırıyor")
        harcanan_mermi = random.randrange(0,10)
        print(str(harcanan_mermi)+" kadar harcandı")
        self.mermi_sayisi -= harcanan_mermi

        return(harcanan_mermi,self.saldırı_gucu)
    
    def saldırıya_ugra(self,gelen_mermi,sg):
        print("Vuruldum")
        self.kalan_can -= (gelen_mermi*sg)

    def mermi_bitti_mi(self):
        if(self.mermi_sayisi <= 0):
            print(self.isim + " konuşuyor : Mermin bitti.Ben kaçar")
            return True
        return False
    
    def hayatta_mi(self):
        if(self.kalan_can <= 0):
            print("Öldüm glb")

    
dusmanlar = []

i = 0
while(i<10):
    rastgelecan = random.randrange(100,200)
    rastgelesg = random.randrange(10,20)
    rastgelemermi = random.randrange(20,30)
    yenidusman = Dusman("Dusman"+str(i+1),rastgelecan,rastgelesg,rastgelemermi)
    dusmanlar.append(yenidusman)
    i += 1

for dusman in dusmanlar:
    dusman.print()

i=0
while(i<3):
    randomdusman1 = random.randrange(0,10)
    randomdusman2 = random.randrange(0,10)

    donendeger = dusmanlar[randomdusman1].saldir()

    dusmanlar[randomdusman2].saldırıya_ugra(donendeger[0],donendeger[1])

    print("round bitti")

    i += 1