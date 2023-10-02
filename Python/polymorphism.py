class Ogrenci():
    def dersCalis(self):
        print("ogrenci ders çalışıyor")


class Calisan():
    def calis(self):
        print("Personel calısıyor")

class Yazilimci(Ogrenci,Calisan):
    pass

yazılımcı = Yazilimci()
yazılımcı.dersCalis()
yazılımcı.calis()