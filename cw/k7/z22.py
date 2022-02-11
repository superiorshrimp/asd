'''
22. Dana jestlista, który być może zakończona jest cyklem.
Napisać funkcję, która sprawdza ten fakt.
'''
'''
class Node:
    def __init__(self, val=None):
        self.val=val
        self.next=None

def utworz_cykl(zbior):
    kopia=zbior
    while True:
        if(kopia.next==None):
            kopia.next=zbior
            return zbior
        kopia=kopia.next
    
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
    i=0
    while(zbior!=None and i<15):
        print(zbior.val,end=" ")
        zbior=zbior.next
        i+=1

def czy_cykl(zbior):
    if(zbior==None):
        return False
    pierwszy=zbior
    kopia=zbior.next
    while(kopia!=None):
        if(kopia==pierwszy):
            return True
        kopia=kopia.next
    return False

zbior=None
zbior=dodaj(zbior, 1)
zbior=dodaj(zbior, 2)
zbior=dodaj(zbior, 3)
zbior=dodaj(zbior, 4)
zbior=dodaj(zbior, 5)
zbior=utworz_cykl(zbior)
print(czy_cykl(zbior))
wypisz(zbior)
#^dziala jesli cala lista stanowi cykl
'''
class Node:
    def __init__(self, val=None):
        self.val=val
        self.next=None

def utworz_cykl(zbior, i):
    kopia=zbior
    licznik=0
    while(licznik!=i):
        kopia=kopia.next
        licznik+=1
    pom=kopia
    kopia=zbior
    while True:
        if(kopia.next==None):
            kopia.next=pom
            return zbior
        kopia=kopia.next
    
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

def wypisz(zbior): #dlugosc cyklu poznamy dopiero w next zad
    i=0
    while(zbior!=None and i<15):
        print(zbior.val,end=" ")
        zbior=zbior.next
        i+=1

def czy_cykl(zbior):
    if(zbior==None or zbior.next==None):
        return False
    l=zbior
    p=zbior
    while(l==None or p==None or p.next!=None or p.next.next!=None):
        l, p = l.next, p.next.next
        if(l==p):
            return True
    return False
    
zbior=None
zbior=dodaj(zbior, 0)
zbior=dodaj(zbior, 1)
zbior=dodaj(zbior, 2)
zbior=dodaj(zbior, 3)
zbior=dodaj(zbior, 4)
zbior=dodaj(zbior, 5)
zbior=utworz_cykl(zbior, 2)
print(czy_cykl(zbior))
wypisz(zbior)