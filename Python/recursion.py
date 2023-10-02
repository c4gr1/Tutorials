def topla(liste):
    toplam = 0

    for i in liste:
        toplam += i

    return toplam

print(topla([1,2,3,4,5]))

def recursiveTopla(liste):
    if(len(liste)==0):
        return 0
    
    else:
        return liste[0] + recursiveTopla(liste[1:])
    

print(topla([7,8,10,15,9]))