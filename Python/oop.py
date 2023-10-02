class Dusman:
    kalan_can = 3
    def saldır(self):
        print("Hucummmmm")
        self.kalan_can -= 1

    def hayatta_mı(self):
        if(self.kalan_can <=0 ):
            print("öldü")
        else:
            print(str(self.kalan_can)+" canın kaldı")

dusman1 = Dusman()
dusman2 = Dusman()

dusman1.saldır()
dusman1.saldır()
dusman1.hayatta_mı()

dusman2.saldır()
dusman2.saldır()
dusman2.saldır()
dusman2.hayatta_mı()