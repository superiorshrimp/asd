'''
28. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
naturalne. W pierwszej liście liczby są posortowane rosnąco, a w drugiej
nie. Proszę napisać funkcję usuwającą z obu list liczby występujące w obu
listach. Do funkcji należy przekazać wskazania na obie listy, funkcja
powinna zwrócić łączną liczbę usuniętych elementów. 
'''
import random

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
    licznik=0
    pom=1
    prev1=None
    kopia1=zbior1
    while(pom==1):
        while(kopia1!=None):
            if(kopia1.val>zbior2.val):
                break
            if(kopia1.val==zbior2.val):
                if(prev1==None):
                    licznik+=1
                    zbior1=zbior1.next
                    zbior2=zbior2.next
                    pom=0
                else:
                    licznik+=1
                    prev1.next=kopia1.next
                    zbior2=zbior2.next
                    pom=0
            prev1=kopia1
            kopia1=kopia1.next
        if(pom==0):
            pom=1
        else:
            pom=0
    prev2=zbior2
    kopia2=zbior2.next
    while(kopia2!=None):
        prev1=None
        kopia1=zbior1
        while(kopia1!=None):
            if(kopia1.val>kopia2.val):
                break
            if(kopia1.val==kopia2.val):
                if(prev1==None):
                    licznik+=1
                    zbior1=zbior1.next
                    prev2.next=kopia2.next
                    break
                else:
                    licznik+=1
                    prev1.next=kopia1.next
                    prev2.next=kopia2.next
                    break
            prev1=kopia1
            kopia1=kopia1.next
        prev2=kopia2
        kopia2=kopia2.next
    print(licznik)
    return zbior1, zbior2


zbior1=None #posortowana
for i in range(1,10):
    zbior1=dodaj(zbior1, 2**i)
zbior2=None #nieposortowana
zbior2=dodaj(zbior2, 32)
zbior2=dodaj(zbior2, 500)
zbior2=dodaj(zbior2, 50)
zbior2=dodaj(zbior2, 1)
zbior2=dodaj(zbior2, 64)
zbior2=dodaj(zbior2, 512)
zbior2=dodaj(zbior2, 507)
zbior2=dodaj(zbior2, 1000)
zbior2=dodaj(zbior2, 784)


zbior1, zbior2 = f(zbior1, zbior2)
wypisz(zbior1)
print()
wypisz(zbior2)
