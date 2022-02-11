'''
7. Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
należy przekazać wskazanie na pierwszy element listy.
'''
class Node:
    def __init__(self, value=None):
        self.val=value
        self.next=None

def wypisz(zbior):
    while(zbior!=None):
        print(zbior.val,end=" ")
        zbior=zbior.next

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

def usun_ostatni(zbior):
    if(zbior==None or zbior.next==None):
        return None
    prev=zbior
    curr=zbior.next
    while(curr.next!=None):
        prev=curr
        curr=curr.next
    prev.next=None
    del curr
    return zbior

zbior=None
for i in range(1,10):
    zbior=dodaj(zbior, 2**i)

zbior=usun_ostatni(zbior)
wypisz(zbior)