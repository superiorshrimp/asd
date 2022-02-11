'''
17. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
początek listy dwukierunkowej, usuwa z niej wszystkie elementy, w których
wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek. 
'''
class Double:
    def __init__(self, val=None, next=None, prev=None):
        self.val=val
        self.next=next
        self.prev=prev

def wypisz(zbior):
    while(zbior!=None):
        print(zbior.val,end=" ")
        zbior=zbior.next

def binarny(n):
    licznik=0
    while(n!=0):
        if(n%2==1):
            licznik+=1
        n//=2
    if(licznik%2==1):
        return True
    return False

def dodaj(first, wartosc):
    kopia=first
    if(first==None):
        first=Double(wartosc)
        return first
    elif(first.next==None):
        kopia=Double(wartosc, None, first)
        first.next=kopia
        return first
    elif(first.next.next==None):
        nowy=Double(wartosc, None, first.next)
        first.next.next=nowy
        return first
    prev=kopia
    kopia=kopia.next
    while(kopia!=None):
        prev=kopia
        kopia=kopia.next
    nowy=Double(wartosc, None, prev)
    prev.next=nowy
    return first

def f(first):
    kopia=first
    if(first==None):
        return first
    elif(first.next==None):
        if(binarny(first.val)==True):
            return None
        else:
            return first
    prev=kopia
    kopia=kopia.next
    while(binarny(prev.val)==True):
        kopia.prev=None
        first=kopia
        return f(first)
    while(kopia!=None):
        if(binarny(kopia.val)==True):
            if(kopia.next!=None):
                prev.next=kopia.next
                kopia.next.prev=prev
                kopia=prev
            else:
                prev.next=kopia.next
                return first
        prev=kopia
        kopia=kopia.next
    return first

first=None
first=dodaj(first, 4)
first=dodaj(first, 9)
first=dodaj(first, 8)
first=dodaj(first, 4)
first=dodaj(first, 17)
first=dodaj(first, 32)
first=f(first)
wypisz(first)