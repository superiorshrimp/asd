'''
11. Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli 
elementu o zadanym kluczu brak w liście należy element o takim kluczu
wstawić do listy.
'''
class Node:
    def __init__(self, val=None):
        self.val=val
        self.next=None

def wypisz(lista):
    kopia=lista
    while(kopia!=None):
        print(kopia.val, end="")
        kopia=kopia.next
    print()

def usun(lista, wartosc):
    if(lista==None):
        return None
    if(lista.val==wartosc):
        kopia=lista
        del lista
        lista=kopia.next
        return lista
    prev=lista
    kopia=lista.next
    while(kopia!=None):
        if(kopia.val==wartosc):
            prev.next=kopia.next
            del kopia
            return lista
        prev=kopia
        kopia=kopia.next
    return lista
    
def dodaj(zbior, element):
    if(zbior==None):
        nowy=Node(element)
        return nowy
    prev=None
    curr=zbior
    while(curr!=None):
        if(curr.val==element):
            return zbior
        prev=curr
        curr=curr.next
    nowy=Node(element)
    prev.next=nowy
    return zbior

def wypisz(zbior):
    while(zbior!=None):
        print(zbior.val,end=" ")
        zbior=zbior.next

def operacja(lista, klucz):
    kopia=lista
    while(kopia!=None):
        if(kopia.val==klucz):
            lista=usun(lista, klucz)
            return lista
        kopia=kopia.next
    lista=dodaj(lista, klucz)
    return lista


lista=None
for i in range(1,10):
    lista=dodaj(lista, 2**i)
lista=operacja(lista, 2)
wypisz(lista)
