sayi1 = input("sayi1:")
sayi2 = input("sayi2:")

try:
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)

    print(sayi1/sayi2)

except (ValueError,ZeroDivisionError):
    print("Bir hata yaklaşıyor efendim")

try:
    dosya = open("deneme.tx","r")
except IOError:
    print("dosya yok")

finally:
    dosya.close()
