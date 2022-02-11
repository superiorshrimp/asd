'''
29. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
naturalne. W obu listach liczby są posortowane rosnąco. Proszę napisać
funkcję usuwającą z każdej listy liczby nie występujące w drugiej. Do
funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić
łączną liczbę usuniętych elementów.
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
    licznik=0
    flag=1
    while(flag==1 and zbior1!=None and zbior2!=None):
        if(zbior1.val==zbior2.val):
            licznik+=1
            zbior1=zbior1.next
            zbior2=zbior2.next
            print("a")
        elif(zbior1.val<zbior2.val):
            prev=zbior1
            kopia=zbior1.next
            while(kopia!=None and kopia.val<=zbior2.val and flag==1):
                if(kopia.val==zbior2.val):
                    licznik+=1
                    prev.next=kopia.next
                    zbior2=zbior2.next
                    flag=0
                    print("b")
                prev=kopia
                kopia=kopia.next
        elif(zbior1.val>zbior2.val):
            prev=zbior2
            kopia=zbior2.next
            while(kopia!=None and kopia.val<=zbior1.val and flag==1):
                if(kopia.val==zbior1.val):
                    licznik+=1
                    prev.next=kopia.next
                    zbior1=zbior1.next
                    flag=0
                    print("c")
                prev=kopia
                kopia=kopia.next
    return
    prev1=zbior1
    kopia1=zbior1.next
    prev2=zbior2
    kopia2=zbior2.next
    while(kopia1!=None and kopia2!=None):
        if(kopia1.val==kopia2.val):
            prev1.next=kopia1.next
            prev2.next=kopia2.next
            licznik+=1
            kopia1=kopia1.next
            kopia2=kopia2.next
            
        elif(kopia1.val<kopia2.val):
            prev1=zbior1
            kopia1=zbior1.next
        else:
            prev2=zbior2
            kopia2=zbior2.next

    print(licznik)
    return zbior1, zbior2

zbior1=None
for i in range(1,10):
    zbior1=dodaj(zbior1, 2**i)
    zbior1=dodaj(zbior1, 2**i+1)
zbior2=None
for i in range(0,50):
    zbior1=dodaj(zbior1, 2*i)

f(zbior1, zbior2)
#zbior1, zbior2 = f(zbior1, zbior2)
wypisz(zbior1)
print()
wypisz(zbior2)
