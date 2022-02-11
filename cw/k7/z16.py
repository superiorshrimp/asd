'''
16. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
początek listy jednokierunkowej, przenosi na początek listy te z nich,
które mają parzystą ilość piątek w zapisie ósemkowym. 
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

def osemkowy(n):
    licznik=0
    while(n!=0):
        if(n%8==5):
            licznik+=1
        n//=8
    if(licznik%2==0):
        return True
    return False

def f(zbior):
    while(zbior!=None):
        if(osemkowy(zbior.val)==False):
            break
        else:
            zbior=zbior.next
    if(zbior==None):
        return None
    elif(zbior.next==None):
        if(osemkowy(zbior.val)==True):
            return None
    prev=zbior
    kopia=zbior.next
    while(kopia!=None):
        if(osemkowy(kopia.val)==True):
            prev.next=kopia.next
            del kopia
            kopia=prev
        prev=kopia
        kopia=kopia.next
    return zbior

zbior=None
for i in range(10):
    zbior=dodaj(zbior, i**3)
zbior=f(zbior)
wypisz(zbior)