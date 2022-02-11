'''
2. Zastosowanie listy odsyłaczowej do implementacji
tablicy rzadkiej. Proszę napisać trzy funkcje:
– inicjalizującą tablicę,
– zwracającą wartość elementu o indeksie n,
– podstawiającą wartość value pod indeks n.
'''
class List:
    def __init__(self, val, next, index): #next=next_non_default
        self.val=val
        self.next=next
        self.index=index

def dodaj(lista, wartosc, id):
    if(id==0):
        lista.val=wartosc
        return lista
    if(lista.next==None):
        lista.next=List(wartosc, None, id)
        return lista

    prev=lista
    kopia=lista.next

    while(kopia!=None):
        if(kopia.index>id):
            break
        prev=kopia
        kopia=kopia.next

    if(prev.index==id):
        prev.val=wartosc
        return lista
    else:
        nowy=List(wartosc, kopia, id)
        prev.next=nowy
        return lista

def wypisz(lista):
    while(lista!=None):
        print(lista.val, "-", lista.index)
        lista=lista.next
    print()

def ity_element(lista, i):
    while(lista!=None):
        if(lista.index==i):
            print(lista.val)
            return
        lista=lista.next
    print("nie ma takiego")

lista=List(0, None, 0)
for i in range(10):
    lista=dodaj(lista, i**2, 5*i)
    lista=dodaj(lista, 989, 16)

#wypisz(lista)

#ity_element(lista, 15)