'''
30. Dane są dwie niepuste listy, z których każda zawiera niepowtarzające
się elementy. Elementy w pierwszej liście są uporządkowane rosnąco, w
drugiej elementy występują w przypadkowej kolejności. Proszę napisać
funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane
elementy będą stanowić sumę mnogościową elementów z list wejściowych.
Do funkcji należy przekazać wskazania na obie listy, funkcja powinna
zwrócić wskazanie na listę wynikową. Na przykład dla list:
2 -> 3 -> 5 ->7-> 11
8 -> 2 -> 7 -> 4
powinna pozostać lista:
2 -> 3 -> 4 -> 5 ->7-> 8 -> 11
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

def f(zbior1, zbior2):
    kopia=zbior2
    while(kopia!=None):
        if(kopia.val<zbior1.val):
            nowy=Node(kopia.val)
            nowy.next=zbior1
            zbior1=nowy
        else:
            prev=None
            z1=zbior1
            while(z1!=None and z1.val<=kopia.val):
                prev=z1
                z1=z1.next
            prev.next=Node(kopia.val)
            prev.next.next=z1
            kopia=kopia.next
    return zbior1

zbior1, zbior2 = None, None
zbior1=dodaj(zbior1, 2)
zbior1=dodaj(zbior1, 3)
zbior1=dodaj(zbior1, 5)
zbior1=dodaj(zbior1, 7)
zbior1=dodaj(zbior1, 11)
zbior2=dodaj(zbior2, 8)
zbior2=dodaj(zbior2, 2)
zbior2=dodaj(zbior2, 7)
zbior2=dodaj(zbior2, 4)
wypisz(f(zbior1, zbior2))
#prawei dobrze