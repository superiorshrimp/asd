'''
9. Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
elementy listy przechowują kolejne cyfry. Proszę napisać funkcję
zwiększającą taką liczbę o 1.
'''
class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=None

def dodaj(liczba, cyfra): #zakladam ze dodawane sa cyfry i pierwsza nie jest 0
    if(liczba==None):
        liczba=Node(cyfra)
        return liczba
    prev=liczba
    kopia=liczba.next
    while(kopia!=None):
        prev=kopia
        kopia=kopia.next
    kopia=Node(cyfra)
    prev.next=kopia
    return liczba
    
def wypisz(liczba):
    while(liczba!=None):
        print(liczba.val, end="")
        liczba=liczba.next
    print()
    return

def push_front(first, val):
    q=Node(val)
    q.next=first
    return q

def f(liczba):
    kopia=liczba
    while(kopia!=None):
        kopia.val+=1
        kopia=kopia.next
    kopia=liczba.next
    prev=liczba
    while(kopia!=None):
        if(kopia.val>9):
            prev.val+=1
            kopia.val-=10
            kopia=liczba
        prev=kopia
        kopia=kopia.next
    while(liczba.val>9):
        liczba.val-=10
        liczba=push_front(liczba, 1+liczba.val//10)
    nowy=liczba
    return liczba
    
liczba=None
for i in range(15):
    liczba=dodaj(liczba, 9)
wypisz(liczba)
w="9"*15
print(int(w)+int(len(w)*'1'))
wypisz(f(liczba))

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

def dodaj_jeden(zbior):
    curr=zbior
    while curr is not None:
        if(curr.val+1==10):
            if(curr.next is not None):
                curr.next.val+=1
                curr.val=0
            else:
                nowy=Node(1)
        curr=curr.next
    return zbior
'''