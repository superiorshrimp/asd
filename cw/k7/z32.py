'''
32. Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w
liście ułożone są według rosnących potęg. Proszę napisać funkcję
obliczającą różnicę dwóch dowolnych wielomianów. Wielomiany reprezentowane
są przez wyżej opisane listy. Procedura powinna zwracać wskaźnik do nowo
utworzonej listy reprezentującej wielomian wynikowy. Listy wejściowe
powinny pozostać niezmienione.
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

def f(liczba1, liczba2):
    wynik=None
    while(liczba1!=None or liczba2!=None):
        if(liczba1==None):
            wynik=dodaj(wynik, -liczba2.val)
            liczba2=liczba2.next
        elif(liczba2==None):
            wynik=dodaj(wynik, liczba1.val)
            liczba1=liczba1.next
        else:
            wynik=dodaj(wynik, liczba1.val-liczba2.val)
            liczba1=liczba1.next
            liczba2=liczba2.next
    return wynik
liczba1, liczba2 = None, None
liczba1 = dodaj(liczba1, 5)
liczba1 = dodaj(liczba1, 3)
liczba1 = dodaj(liczba1, 7)
liczba1 = dodaj(liczba1, 8)
liczba2 = dodaj(liczba2, 5)
liczba2 = dodaj(liczba2, 56)
liczba2 = dodaj(liczba2, 2)
wypisz(f(liczba1, liczba2))