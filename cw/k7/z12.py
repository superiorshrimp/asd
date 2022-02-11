'''
12. Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci
jednokierunkowej listy. Napisy w łańcuchu są uporządkowane
leksykograficznie. Proszę napisać stosowne definicje typów oraz funkcję
dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy
oraz wstawiany napis, funkcja powinna zwrócić wartość logiczną wskazującą,
czy w wyniku operacji moc zbioru uległa zmianie.
'''
'''
class Node:
    def __init__(self, val=None):
        self.val=val
        self.next=None

def wypisz(zbior):
    while(zbior!=None):
        print(zbior.val, end=" ")
        zbior=zbior.next

def leksykograficznie(a, b):
    l=ord(a[0])
    p=ord(b[0])
    if(l<p):
        return a
    elif(l>p):
        return b
    i=1
    while(l==p):
        if(i==len(a)):
            return a
        elif(i==len(b)):
            return b
        else:
            l=ord(a[i])
            p=ord(b[i])
        i+=1
    else:
        if(l<p):
            return a
        elif(l<p):
            return b

def dodaj(zbior, napis):
    if(zbior==None):
        zbior=Node(napis)
        return zbior
    kopia=zbior
    if(leksykograficznie(kopia.val, napis)==napis):
        zbior=Node(napis)
        zbior.next=kopia
        return zbior
    else:
        kopia=Node(napis)
        zbior.next=kopia
        return zbior
    prev=kopia
    kopia=kopia.next
    while(kopia!=None):
        if(leksykograficznie(kopia.val, napis)==napis):
            pom=Node(napis)
            prev.next=pom
            pom.next=kopia
            return zbior
        prev=kopia
        kopia=kopia.next
    pom=Node(napis)
    prev.next=pom
    pom.next=kopia
    return zbior

zbior=None
zbior=dodaj(zbior, "kot")
zbior=dodaj(zbior, "koty")
zbior=dodaj(zbior, "ala")
wypisz(zbior)
'''
