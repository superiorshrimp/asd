'''
20. Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów.
Krańce przedziałów określa uporządkowana para liczb całkowitych. Proszę
napisać stosowne deklaracje oraz funkcję redukującą liczbę elementów listy.
Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17]
powinien zostać zredukowany do listy: [13,19] [2,6] [7,12]
'''
class Node:
    def __init__(self, a, b, next=None):
        self.a=a
        self.b=b
        self.next=next

def dodaj(zbior, a, b):
    if(zbior==None):
        nowy=Node(a, b)
        return nowy
    prev=None
    curr=zbior
    while(curr!=None):
        if(curr.a==a and curr.b==b):
            return zbior
        prev=curr
        curr=curr.next
    nowy=Node(a, b)
    prev.next=nowy
    return zbior

def wypisz(zbior):
    while(zbior!=None):
        print(zbior.a,zbior.b,end=" ")
        zbior=zbior.next

def f(zbior):
    if(zbior==None or zbior.next==None):
        return zbior
    else:
        kopia=zbior
        while(kopia!=None):
            prev=kopia
            sprawdzany=kopia.next
            while(sprawdzany!=None):
                if((kopia.a<=sprawdzany.a and kopia.b>=sprawdzany.a) or (kopia.a>=sprawdzany.a and kopia.a<=sprawdzany.b)):
                    kopia.a=min(kopia.a, sprawdzany.a)
                    kopia.b=max(kopia.b, sprawdzany.b)
                    prev.next=sprawdzany.next
                    del sprawdzany
                    sprawdzany=prev
                prev=sprawdzany
                sprawdzany=sprawdzany.next

            kopia=kopia.next
        return zbior

zbior=None
#T=[[2,7], [1,5]]
T=[[15,19], [2,5], [7,11], [8,12], [5,6], [13,17]]
for k in T:
    zbior=dodaj(zbior, k[0], k[1])
zbior=f(zbior)
wypisz(zbior)

