'''
15. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
początek listy jednokierunkowej, usuwa z niej wszystkie elementy, w których
wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek. 
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

def trojkowy(n):
    licznik1=0
    licznik2=0
    while(n!=0):
        if(n%3==1):
            licznik1+=1
        elif(n%3==2):
            licznik2+=1
        n//=3
    if(licznik1>licznik2):
        return True
    return False

def f(zbior):
    while(zbior!=None):
        if(trojkowy(zbior.val)==False):
            break
        else:
            zbior=zbior.next
    if(zbior==None):
        return None
    elif(zbior.next==None):
        if(trojkowy(zbior.val)==True):
            return None
    prev=zbior
    kopia=zbior.next
    while(kopia!=None):
        if(trojkowy(kopia.val)==True):
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