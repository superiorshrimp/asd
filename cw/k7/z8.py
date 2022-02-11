'''
8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
element listy. Do funkcji należy przekazać wskazanie na pierwszy element
listy.
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

def usun_co_drugi(zbior):
    curr=zbior
    i=0
    while(curr!=None):
        if(i%2==1):
            prev.next=curr.next
        prev=curr   
        curr=curr.next
        i+=1
    return zbior


zbior=None
for i in range(1,10):
    zbior=dodaj(zbior, 2**i)
zbior=usun_co_drugi(zbior)
wypisz(zbior)

