'''
31. Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza
powinna zawierać klucze parzyste dodatnie, drugi klucze nieparzyste ujemne,
pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać
wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja
powinna zwrócić liczbę usuniętych elementów. 
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

def f(zbior):
    licznik=0
    ujemne=None
    dodatnie=None
    prev=None
    while(zbior!=None):
        if(zbior.val<0 and zbior.val%2==1):
            ujemne=dodaj(ujemne, zbior.val)
        elif(zbior.val>0 and zbior.val%2==0):
            dodatnie=dodaj(dodatnie, zbior.val)
        else:
            licznik+=1
            prev.next=zbior.next
            del zbior
            zbior=prev
        prev=zbior
        zbior=zbior.next
    print(licznik)
    return ujemne, dodatnie


zbior=None
for i in range(-5, 6):
    zbior=dodaj(zbior, i)
ujemne, dodatnie = f(zbior)
wypisz(ujemne)
print("bruv")
wypisz(dodatnie)