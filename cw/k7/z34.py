'''
34. Proszę napisać funkcję, która usuwa z listy cyklicznej elementy,
których klucz występuje dokładnie k razy. Do funkcji należy przekazać
wskazanie na jeden z elementów listy, oraz liczbę k, funkcja powinna
zwrócić informację czy usunięto jakieś elementy z listy. 
'''
class Node:
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next

def dodaj(zbior, element):
    if(zbior==None):
        nowy=Node(element)
        return nowy
    prev=None
    curr=zbior
    while(curr!=None):
        prev=curr
        curr=curr.next
    nowy=Node(element)
    prev.next=nowy
    return zbior

def utworz_cykl(zbior):
    kopia=zbior
    pom=zbior
    while True:
        if(kopia.next==None):
            kopia.next=pom
            return zbior
        kopia=kopia.next

def wypisz(zbior):
    for _ in range(15):
        print(zbior.val, end=" ")
        zbior=zbior.next
    print()
    return

def f(zbior, k):
    kopia1=zbior
    kopia2=zbior.next
    dl=0
    while(kopia1!=kopia2):
        kopia2=kopia2.next
        dl+=1
    pom=dl
    cp=dl
    licznik=1
    kopia1=zbior
    kopia2=zbior.next
    while(pom>0):
        while(cp>0):
            if(kopia1.val==kopia2.val):
                licznik+=1
            kopia2=kopia2.next
            cp-=1
        if(licznik==k):
            i=0
            prev=kopia2
            curr=kopia2.next
            while(i<licznik):
                if(curr.val==kopia1.val):
                    prev.next=curr.next
                    curr=prev
                prev=curr
                curr=curr.next
            pom-=k
            dl-=k
        pom-=1
        cp=dl
        licznik=1
        kopia1=kopia1.next
        kopia2=kopia1.next
    wypisz(zbior)
    
    print(T)
    exit(0)
        


zbior=None
zbior=dodaj(zbior, 1)
zbior=dodaj(zbior, 2)
zbior=dodaj(zbior, 1)
zbior=dodaj(zbior, 3)
zbior=dodaj(zbior, 1)
zbior=dodaj(zbior, 4)
zbior=dodaj(zbior, 5)
zbior=dodaj(zbior, 2)
zbior=utworz_cykl(zbior)
wypisz(f(zbior, 3))
