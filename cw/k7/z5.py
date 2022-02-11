'''
5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
należy połączyć w jedną listę odsyłaczową, która jest posortowana
niemalejąco według ostatniej cyfry pola val.
'''
import random

class Node:
    def __init__(self, value=None):
        self.val=value
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

def podzial(zbior, T):
    if(zbior==None):
        return T
    curr=zbior
    while(curr!=None):
        T[curr.val%10]=dodaj(T[curr.val%10], curr.val) #glupio mozna zrobic liste lastow
        curr=curr.next
    return T

def dodaj_zbior(first, zbior):
    if(first==None):
        return zbior
    curr=first
    while(curr.next!=None):
        prev=curr
        curr=curr.next
    curr.next=zbior
    return first

zbior=None
for i in range(100):
    zbior=dodaj(zbior, random.randint(1, 100))

T=[None for _ in range(10)]

T=podzial(zbior, T)

nowy=None

for k in T:
    nowy=dodaj_zbior(nowy, k)

wypisz(nowy)