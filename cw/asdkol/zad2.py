#Szymon Żychowicz
'''
wykonuję n razy (n - długość Node) selection sorta na Node'ach długości k+1 (zmienia się to dla ostatnich porównań, ale dla notacji O nie ma to znaczenia)
sprawia to, że moje rozwiązanie ma złożoność O(k*n)
jeśli k będzie rzędu O(1) to złożoność będzie O(n)
jeśli k będzie rzędu O(logn) to złożoność będzie O(nlogn)
jeśli k będzie rzędu O(n) to złożoność będzie O(n^2), chyba że wprowadzimy następującą modyfikację (średni czas dla innych przpadków wzrośnie i będziemy używać O(n) dodatkowej pamięci):
1) zliczamy długość Node
2) jeśli k jest rzędu O(n) w stosunku do licznika (nie O(logn), bo wtedy lepiej użyć kodu poza komentarzem, bo nie trzeba dodatkowej pamieci O(n) i dla O(logn) pivot będzie dobierany nieoptymalnie)
to O(n) zczytujemy wartosci z Node do tablicy T
3) następnie wykonujemy quick sorta na T (nlogn) i całkowita złożoność to właśnie nlogn i n pamięci)
4) ostatnim krokiem jest odwrotność funkcji zczytaj czyli z posortowanej T układamy Node
żeby nie być gołosłownym wklejam taką modyfikację (kod działa; przyjąłem, że k musi stanowić min połowę n aby użyć qs):
from zad2testy import runtests

class Node:
  def __init__(self):
    self.val = None     
    self.next = None 

def zczytaj(head, licznik):
    T=[0]*licznik
    i=0
    while i<licznik:
        T[i]=head.val
        i+=1
        head=head.next
    return T

def zczytaj_odwrotnie(T, licznik):
    head=Node()
    head.val=T[0]
    prev=head
    curr=None
    i=1
    while i<licznik:
        curr=Node()
        curr.val=T[i]
        i+=1
        prev.next=curr
        prev=curr
    return head

def partition(T, l, p):
    pivot=T[p]
    j=l
    for i in range(l, p):
        if(T[i]<=pivot):
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def quicksort(T): #iteracyjnie
    l=0
    p=len(T)-1
    stack=[0]*len(T)
    stack[0]=[l, p]
    top=0
    while top>=0:
        l, p = stack[top]
        top-=1
        q=partition(T, l, p)
        if q-1>l:
            top+=1
            stack[top]=[l, q-1]
        if q+1<p:
            top+=1
            stack[top]=[q+1, p]
    return T

def f(head):
    licznik=0
    while head is not None:
        head=head.next
        licznik+=1
    return licznik

def SortH(p, k):
    head=p
    licznik=f(head)
    if licznik/2<k:
        T=zczytaj(head, licznik)
        quicksort(T)
        head=zczytaj_odwrotnie(T, licznik)
    else:
        curr=head
        j=k
        prev=None
        min_prev=None
        min=curr.val
        while curr is not None and j>=0:
            if curr.val<min:
                min=curr.val
                min_prev=prev
            prev=curr
            curr=curr.next
            j-=1
        if min_prev is not None:
            new=min_prev.next
            min_prev.next=min_prev.next.next
            new.next=head
            head=new
        curr=head
        while curr.next is not None:
            j=k
            cp=curr.next
            prev=curr
            min=cp.val
            min_prev=curr
            while cp is not None and j>=0:
                if cp.val<min:
                    min=cp.val
                    min_prev=prev
                prev=cp
                cp=cp.next
                j-=1
            new=min_prev.next
            min_prev.next=min_prev.next.next
            new.next=curr.next
            curr.next=new
            curr=curr.next
    return head

runtests( SortH )
'''

from zad2testy import runtests

class Node:
  def __init__(self):
    self.val = None     
    self.next = None 

def SortH(p, k):
    head=p
    curr=head
    j=k
    prev=None
    min_prev=None
    min=curr.val
    while curr is not None and j>=0:
        if curr.val<min:
            min=curr.val
            min_prev=prev
        prev=curr
        curr=curr.next
        j-=1
    if min_prev is not None:
        new=min_prev.next
        min_prev.next=min_prev.next.next
        new.next=head
        head=new
    curr=head
    while curr.next is not None:
        j=k
        cp=curr.next
        prev=curr
        min=cp.val
        min_prev=curr
        while cp is not None and j>=0:
            if cp.val<min:
                min=cp.val
                min_prev=prev
            prev=cp
            cp=cp.next
            j-=1
        new=min_prev.next
        min_prev.next=min_prev.next.next
        new.next=curr.next
        curr.next=new
        curr=curr.next
    return head

runtests( SortH ) 