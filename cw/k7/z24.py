'''
24. Dana jest lista, który zakończona jest cyklem.
Napisać funkcję, która zwraca liczbę elementów przed cyklem.
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

def wypisz(zbior):
    i=0
    while(zbior!=None and i<15):
        print(zbior.val,end=" ")
        zbior=zbior.next
        i+=1

def dl_cyklu(zbior):
    if(zbior==None or zbior.next==None):
        return 0
    l=zbior
    p=zbior
    while(l==None or p==None or p.next!=None or p.next.next!=None):
        l, p = l.next, p.next.next
        if(l==p):
            licznik=1
            while True:
                zbior=zbior.next
                if(zbior==l):
                    return licznik
                licznik+=1
    return 0
    
def dl_przed_cyklem(zbior, dl):
    kopia=zbior
    licznik=1
    while True:
        i=0
        pom=kopia
        while(i<=dl):
            pom=pom.next
            i+=1
        if(pom==kopia):
            return licznik
        licznik+=1
        kopia=kopia.next

zbior=None
zbior=dodaj(zbior, 0)
zbior=dodaj(zbior, 1)
zbior=dodaj(zbior, 2)
zbior=dodaj(zbior, 3)
zbior=dodaj(zbior, 4)
zbior=dodaj(zbior, 5)
zbior=utworz_cykl(zbior, 2)
dl=dl_cyklu(zbior)
if(dl!=0):
    print(dl_przed_cyklem(zbior, dl-1))
wypisz(zbior)