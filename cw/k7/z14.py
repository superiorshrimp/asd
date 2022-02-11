'''
14. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
element listy o wartościach typu int, usuwającą wszystkie elementy, których
wartość dzieli bez reszty wartość bezpośrednio następujących po nich
elementów
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

def f(zbior):
    if(zbior==None or zbior.next==None):
        return zbior
    prev=zbior
    curr=zbior.next
    while(curr.val%prev.val==0 or curr==None):
        print("a")
        del prev
        zbior=curr
        prev=curr
        curr=curr.next
    while(curr.next!=None):
        if(curr.next.val%curr.val==0):
            prev.next=curr.next
            del curr
            curr=prev
        prev=curr
        curr=curr.next
    return zbior

zbior=None
zbior=dodaj(zbior, 1)
zbior=dodaj(zbior, 7)
zbior=dodaj(zbior, 49)
zbior=dodaj(zbior, 5)
zbior=dodaj(zbior, 15)
zbior=dodaj(zbior, 3)
zbior=dodaj(zbior, 12)
zbior=dodaj(zbior, 8)
zbior=f(zbior)
wypisz(zbior)