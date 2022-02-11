'''
18. Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.
'''
'''
#lista--->zbior
class Node:
    def __init__(self, val=None):
        self.val=val
        self.next=None

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

def usun(zbior, element, licznik):
    if(zbior.val==element):
        del zbior
        return None
    p=0
    prev=zbior
    curr=zbior.next
    while(curr!=None):
        if(curr.val==element and licznik==p):
            prev.next=curr.next
            del curr
        prev=curr
        curr=curr.next
        p+=1
    return zbior

def f(zbior):
    if(zbior==None):
        return None
    if(zbior.next==None):
        return zbior
    licznik=0
    prev=zbior
    kopia=zbior.next
    while(kopia!=None):
        wartosc=kopia.val
        kopia=usun(kopia, wartosc, licznik)
        if(kopia==None):
            return zbior
        prev=kopia
        kopia=kopia.next
        licznik+=1
    return zbior

zbior=None
for i in range(1,10):
    zbior=dodaj(zbior,i//2)
    zbior=dodaj(zbior,7)
    zbior=dodaj(zbior, 2**i)
zbior=f(zbior)
wypisz(zbior)
'''
class Node:
    def __init__(self, val=None):
        self.val=val
        self.next=None

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

def usun(zbior, element):
    if(zbior.val==element):
        del zbior
        return None
    prev=zbior
    curr=zbior.next
    while(curr!=None):
        if(curr.val==element):
            prev.next=curr.next
            curr=curr.next
            if(curr==None):
                return zbior        
        prev=curr
        curr=curr.next
    return zbior

def f(zbior):
    if(zbior==None):
        return None
    if(zbior.next==None):
        return zbior
    prev=zbior
    kopia=zbior.next
    while(kopia!=None):
        wartosc=kopia.val
        prev=usun(prev, wartosc)
        if(prev.next==None):
            return zbior
        prev=kopia
        kopia=kopia.next
    return zbior

zbior=None
for i in range(1,10):
    zbior=dodaj(zbior,i//2)
    zbior=dodaj(zbior,7)
    zbior=dodaj(zbior, 2**i)
zbior=f(zbior)
wypisz(zbior)