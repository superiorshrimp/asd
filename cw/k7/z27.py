'''
27. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
- funkcja iteracyjna,
- funkcja rekurencyjna
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

def scal(zbior1, zbior2):
    if(zbior1==None):
        return zbior2
    elif(zbior2==None):
        return zbior1
    if(zbior1.val<zbior2.val):
        first=zbior1
        kopia1=zbior1.next
        kopia2=zbior2
    elif(zbior1.val>zbior2.val):
        first=zbior2
        kopia1=zbior1
        kopia2=zbior2.next
    else:
        first=zbior1
        kopia1=zbior1.next
        kopia2=zbior2.next
    nowy=first
    while True:
        if(kopia1==None):
            nowy.next=kopia2
            return first
        elif(kopia2==None):
            nowy.next=kopia1
            return first
        if(kopia1.val<kopia2.val):
            nowy.next=kopia1
            nowy=kopia1
            kopia1=kopia1.next
            kopia2=kopia2
        elif(kopia1.val>kopia2.val):
            nowy.next=kopia2
            nowy=kopia2
            kopia1=kopia1
            kopia2=kopia2.next
        else:
            nowy.next=kopia1
            nowy=kopia1
            kopia1=kopia1.next
            kopia2=kopia2.next


zbior1=None
for i in range(1,10):
    zbior1=dodaj(zbior1, 2**i)
zbior2=None
for i in range(2**9+1):
    zbior2=dodaj(zbior2, 2*i)
scalony=scal(zbior1, zbior2)
wypisz(scalony)