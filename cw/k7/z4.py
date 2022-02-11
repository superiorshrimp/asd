'''
4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
kolejność jej elementów.
'''
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

def odwroc_rek(zbior, prev):
    if(zbior.next==None):
        return dodaj(None, zbior.val)
    prev=zbior
    zbior=zbior.next
    return dodaj(odwroc_rek(zbior, prev), prev.val)

def odwroc(zbior):
    if(zbior==None):
        return None
    
    return odwroc_rek(zbior, None)

zbior=None
for i in range(1,10):
    zbior=dodaj(zbior, 2**i)

nowy=odwroc(zbior)

wypisz(nowy)