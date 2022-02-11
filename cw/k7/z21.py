'''
21. Kolejne elementy listy o zwiększającej się wartości pola val nazywamy
podlistą rosnącą. Proszę napisać funkcję, która usuwa z listy wejściowej
najdłuższą podlistę rosnącą. Warunkiem usunięcia jest istnienie w liście
dokładnie jednej najdłuższej podlisty rosnącej. 
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

def usun_podciag_rosnacy(zbior, first, i, prev):
    while(i!=0):
        first=first.next
        i-=1
    prev.next=first
    return zbior

def wypisz(zbior):
    while(zbior!=None):
        print(zbior.val,end=" ")
        zbior=zbior.next

def f(zbior):
    if(zbior==None or zbior.next==None):
        return None
    kopia=zbior.next
    prev=zbior
    licznik=1
    max=1
    stop=1
    first_pom=kopia
    prev_pom=prev
    while(kopia!=None):
        print(licznik)
        if(kopia.val>prev.val):
            licznik+=1
            if(licznik>max):
                u_first=first_pom
                u_prev=prev_pom
                max=licznik
                stop=0
            elif(licznik==max):
                max=licznik
                stop=1
        else:
            licznik=0
            first_pom=kopia.next
            prev_pom=kopia
        kopia=kopia.next
    if(stop==0):
        return usun_podciag_rosnacy(zbior, u_first, max, u_prev)
    else:
        return zbior


zbior=None
for i in range(1,10):
    zbior=dodaj(zbior, i)
zbior=f(zbior)
wypisz(zbior)
#nie dziala