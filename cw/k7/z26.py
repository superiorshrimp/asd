'''
26. Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w
drugiej. Do funkcji należy przekazać wskazania na pierwsze elementy obu
list, funkcja powinna zwrócić wartość logiczną.
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

def zawieranie(zbior1, zbior2):
    if(zbior1==None or zbior2==None):
        return True
    kopia1=zbior1
    while(kopia1!=None):
        if(czy_nalezy(zbior2, kopia1.val)==False): #jesli false to znaczy ze zbior1 nie zawiera sie w zbiorze2 
            kopia2=zbior2
            while(kopia2!=None):
                if(czy_nalezy(zbior1, kopia2.val)==False):
                    return False
                kopia2=kopia2.next
            return True
        kopia1=kopia1.next
    return True

zbior1=None
for i in range(1,10):
    zbior1=dodaj(zbior1, 2**i)
zbior2=None
for i in range(2**9+1):
    zbior2=dodaj(zbior2, 2*i)
print(zawieranie(zbior1, zbior2))