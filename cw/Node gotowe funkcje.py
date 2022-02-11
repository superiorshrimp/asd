class Node:
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next

def utworz_linkliste_z_listy(T):
    if(len(T)==0):
        return None
    zbior=Node(T[0])
    kopia=zbior
    for k in T[1:]:
        nowy=Node(k)
        kopia.next=nowy
        kopia=kopia.next
    return zbior

def wypisz(zbior):
    if zbior is None:
        print("pusty")
        return
    while zbior is not None:
        print(zbior.val, end=" ")
        zbior=zbior.next
    print()
    return

def dodaj(zbior, wartosc):
    nowy=Node(wartosc)
    if zbior is None:
        return nowy
    kopia=zbior
    while kopia.next is not None:
        kopia=kopia.next
    kopia.next=nowy
    return zbior

def dodaj_na_poczatek(zbior, wartosc): #uwaga: w klasie musi byc next do dodania
    if zbior is None:
        nowy=Node(wartosc)
        return nowy
    nowy=Node(wartosc, zbior)
    return nowy

def znajdz_element(zbior, szukany): #zwraca False albo True; szuka po wartosci
    if zbior is None:
        return False
    while zbior is not None:
        if(zbior.val==szukany):
            return True
        zbior=zbior.next
    return False

def idz_do_ostatniego(zbior):
    if zbior is None:
        return None
    while zbior.next is not None:
        zbior=zbior.next
    return zbior

def znajdz_poprzedni(zbior, element): #po wartosci
    if zbior is None or zbior.next is None or zbior.val==element:
        return None
    while zbior.next is not None:
        if(zbior.next.val==element):
            return zbior
        zbior=zbior.next

def znajdz_poprzedni_po_objekcie(zbior, element): #po objekcie
    if zbior is None or zbior.next is None or zbior==element:
        return None
    while zbior.next is not None:
        if(zbior.next==element):
            return zbior
        zbior=zbior.next

def polacz(zbior1, zbior2, ostatni1): #znany ostatni
    if zbior1 is None:
        return zbior2
    elif zbior2 is None:
        return zbior1
    ostatni1.next=zbior2
    return zbior1

def polacz(zbior1, zbior2): #nieznany ostatni element
    if zbior1 is None:
        return zbior2
    elif zbior2 is None:
        return zbior1
    kopia=zbior1
    while kopia.next is not None:
        kopia=kopia.next
    kopia.next=zbior2
    return zbior1

def insert(zbior, wartosc): #w posortowanej liscie po wartosci
    if zbior is None:
        nowy=Node(wartosc)
        return nowy
    kopia=zbior
    while kopia.next is not None:
        if(kopia.next.val<wartosc):
            nowy=Node(wartosc, kopia.next.next)
            kopia.next=nowy
    return zbior

def insert_po_objekcie(zbior, element, prev):
    if zbior is None:
        return element
        element.next=None
    if prev is None:
        element.next=zbior
        return element
    if prev.next is None:
        element.next=None
        prev.next=element
        return zbior
    element.next=prev.next.next
    prev.next=element
    return zbior

def usun(zbior, wartosc): #po wartosci
    if zbior is None:
        return zbior
    if zbior.next is None:
        if(zbior.next.val==wartosc):
            del zbior
            return None
    prev=zbior
    kopia=zbior.next
    while kopia is not None:
        if(kopia.val==wartosc):
            prev.next=kopia.next
            del kopia
            return zbior
        kopia=kopia.next
    return zbior

def swap(zbior, prev1, prev2):
    if zbior is None or zbior.next is None:
        return zbior
    if prev1 is None:
        kopia1=zbior
        kopia2=prev2.next
        prev2.next=kopia1
        kopia1.next, kopia2.next= kopia2.next, kopia1.next 
        return kopia2
    elif prev2 is None:
        kopia2=zbior
        kopia1=prev1.next
        prev1.next=kopia2
        kopia2.next, kopia1.next= kopia1.next, kopia2.next 
        return kopia1
    kopia1=prev1.next
    kopia2=prev2.next
    prev1.next, prev2.next = kopia2, kopia1
    kopia1.next, kopia2.next = kopia2.next, kopia1.next
    return zbior

zb=None
for i in range(5):
    zb=dodaj(zb, i)
zb=dodaj_na_poczatek(zb, -1)
wypisz(zb)
zbior=utworz_linkliste_z_listy([1, 2, 4, 6, 8, 10, 12])
print(znajdz_element(zbior, 0))
pom1=idz_do_ostatniego(zbior)
print(pom1.val)
pom2=znajdz_poprzedni(zbior, 8)
print(pom2.val)
zbior=polacz(zbior, zb)
wypisz(zbior)

kopia=zbior
i=0
prev2=None
while kopia is not None:
    if i==200:
        prev2=kopia
    if i==0:
        prev1=kopia
    kopia=kopia.next
    i+=1

wypisz(swap(zbior, prev1, prev2))