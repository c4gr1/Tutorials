class Calisan():
    def __init__(self,isim,maas,departman):
        print("Calisan sınıfının yapici fonksiyonu")
        self.isim=isim
        self.maas=maas
        self.departman=departman

    def bilgilerigoster(self):
        print("Calisanin bilgileri gösteriliyor....")
        print("İsim :",self.isim)
        print("Maas :",self.maas)
        print("Departman :",self.departman)
    
    def maasazamyap(self,zammiktari):
        print("Maaşa zam yapıldı")
        self.maas += zammiktari

    def departmandegistir(self,yeni):
        print("departman değiştiriliyor....")
        self.departman = yeni

calisan = Calisan("X",2500,"Astronot")
calisan.bilgilerigoster()

class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisi_sayisi):
        print("Yonetici sınıfının yapici fonksiyonu")
        super().__init__(isim,maas,departman)
        self.kisi_sayisi=kisi_sayisi

    def bilgilerigoster(self):
        print("Yoneticinin bilgileri gösteriliyor....")
        print("İsim :",self.isim)
        print("Maas :",self.maas)
        print("Departman :",self.departman)
        print("Kişi Sayısı :",self.kisi_sayisi)

    def kisiSayisiArttir(self,arttır):
        ("Kişi sayısı arttırlıyor")
        self.kisi_sayisi += arttır

yonetici = Yonetici("Y",1700,"Emekli",0)
yonetici.bilgilerigoster()
yonetici.kisiSayisiArttir(15)
yonetici.bilgilerigoster()