'''
Yöntem 1
import moduls

moduls.naber()

print(moduls.mutlakDeger(-789))
'''

#Yöntem 2 : bu cok tercih edilmiyor cunku moduls2 dosyamız olsa
#ve onda da naber fonksiyonu olsa karışıklık oluyor
from moduls import *
import math

naber()
mutlakDeger(-1)
print(math.factorial(10))

