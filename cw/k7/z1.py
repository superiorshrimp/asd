'''
1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
struktury listy odsyłaczowej.
- czy element należy do zbioru
- wstawienie elementu do zbioru
- usunięcie elementu ze zbioru
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

def czy_nalezy(zbior, element):
    while(zbior!=None):
        if(zbior.val==element):
            return True
        zbior=zbior.next
    return False

def usun(zbior, element):
    if(zbior.val==element):
        del zbior
        return None
    prev=zbior
    curr=zbior.next
    while(curr!=None):
        if(curr.val==element):
            prev.next=curr.next
            del curr
            return zbior
        prev=curr
        curr=curr.next
    return zbior

zbior=None
for i in range(1,10):
    zbior=dodaj(zbior, 2**i)
zbior=usun(zbior, 8)
wypisz(zbior)