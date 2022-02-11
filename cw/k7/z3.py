'''
3. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
- funkcja iteracyjna,
- funkcja rekurencyjna.
'''
'''
def scal_iter(first, pierwszy):
    nowy=None
    curr=first
    akt=pierwszy
    while(curr!=None and akt!=None):
        if(curr.val<akt.val):
            nowy=dodaj(nowy, curr.val)
            curr=curr.next
        else:
            nowy=dodaj(nowy, akt.val)
            akt=akt.next
    if(curr==None):
        while(akt!=None):
            nowy=dodaj(nowy, akt.val)
            akt=akt.next
    elif(akt==None):
        while(curr!=None):
            nowy=dodaj(nowy, curr.val)
            curr=curr.next
    return nowy
'''
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
    print()

def scal_rek(first, pierwszy, curr, akt, nowy):
    if(curr==None and akt==None):
        return nowy
    if(curr!=None and akt!=None):
        if(curr.val<akt.val):
            nowy=dodaj(nowy, curr.val)
            return scal_rek(first, pierwszy, curr.next, akt, nowy)
        else:
            nowy=dodaj(nowy, akt.val)
            return scal_rek(first, pierwszy, curr, akt.next, nowy)
    elif(curr==None):
        while(akt!=None):
            nowy=dodaj(nowy, akt.val)
            return scal_rek(first, pierwszy, curr, akt.next, nowy)
    else:
        while(curr!=None):
            nowy=dodaj(nowy, curr.val)
            return scal_rek(first, pierwszy, curr.next, akt, nowy)

def scal(first, pierwszy):
    return scal_rek(first, pierwszy, first, pierwszy, None)

first=None
pierwszy=None
for i in range(1, 10):
    first=dodaj(first, i)
    pierwszy=dodaj(pierwszy, 2*(i-2))
wypisz(first)
wypisz(pierwszy)

nowy=scal(first, pierwszy)
wypisz(nowy)
'''
#scalanie - elementy moga sie powtarzac
#rekurencyjnie
class Node:
    def __init__(self, val=None):
        self.val=val
        self.next=None

def scal_rek(l1, l2):
    if(l1==None):
        return l2
    if(l2==None):
        return l1
    if(l1.val<l2.val):
        res=l1
        res.next=scal_rek(l1.next, l2)
    else:
        res=l2
        res.next=scal_rek(l1, l2.next)
    return res