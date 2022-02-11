'''
13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
element listy o wartościach typu int, usuwającą wszystkie elementy, których
wartość jest mniejsza od wartości bezpośrednio poprzedzających je
elementów. 
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

def usun(prev, curr):
    prev.next=curr.next
    del curr
    return prev

def f(zbior):
    if(zbior==None or zbior.next==None):
        return zbior
    prev=zbior
    curr=zbior.next
    while(curr!=None):
        while(curr.val<prev.val):
            curr=usun(prev, curr)
        prev=curr
        curr=curr.next
    return zbior

zbior=None
zbior=dodaj(zbior, 2)
zbior=dodaj(zbior, 1)
zbior=dodaj(zbior, 5)
zbior=dodaj(zbior, 3)
zbior=dodaj(zbior, 4)
zbior=dodaj(zbior, 9)
zbior=dodaj(zbior, 6)
zbior=dodaj(zbior, 7)
zbior=dodaj(zbior, 11)
zbior=f(zbior)
wypisz(zbior)
'''

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

def f(zbior):
    if zbior is None or zbior.next is None:
        return zbior
    prev=zbior
    curr=zbior.next
    bufor=zbior.val
    while curr is not None:
        if(curr.val<bufor):
            bufor=curr.val
            prev.next, curr = curr.next, curr.next
        else:
            bufor=curr.val
            prev=curr
            curr=curr.next
    return zbior
        
zbior=utworz_linkliste_z_listy([5, 4, 4, 3, 5, 2, 1])
wypisz(f(zbior))        
