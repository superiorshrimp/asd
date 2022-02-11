'''
33. Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza”
od pierwszej litery s2. Według tej zasady rozmieszczono napisy w liście
cyklicznej, na przykład:
┌─bartek──leszek──marek──ola──zosia─┐
└───────────────────────────────────┘
Proszę napisać stosowne definicje typów oraz funkcję wstawiającą do listy
napis z zachowaniem zasady poprzedzania. Do funkcji należy przekazać
wskaźnik do listy oraz wstawiany napis, funkcja powinna zwrócić wartość
logiczną wskazującą, czy udało się wstawić napis do listy. Po wstawieniu
elementu wskaźnik do listy powinien wskazywać na nowo wstawiony element.
'''

class Node:
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next

def utworz_linkliste_z_listy(T):
    if(len(T)==0):
        return None
    zbior=Node(T[0])
    kopia=zbior
    for k in T[1:]:
        nowy=Node(k)
        kopia.next=nowy
        kopia=kopia.next
    return zbior

def wypisz(zbior):
    if zbior is None:
        print("pusty")
        return
    for _ in range(10):
        print(zbior.val, end=" ")
        zbior=zbior.next
    print()
    return

def czy_poprzedza(napis1, napis2):
    if(ord(napis1[-1])<ord(napis2[0])):
        return True
    return False

#┌─bartek──leszek──marek──ola──zosia─┐
#└───────────────────────────────────┘

def f(zbior, napis): #napis to obiekt
    if zbior is None:
        napis.next=napis
        return True
    elif(zbior==zbior.next):
        if(czy_poprzedza(zbior.val, napis.val) is True and czy_poprzedza(napis.val, zbior.val) is True):
            zbior.next=napis
            napis.next=zbior
            return True
        else:
            return False
    prev=zbior
    kopia=zbior.next
    while(kopia!=zbior):
        if(czy_poprzedza(prev.val, napis.val) is True and czy_poprzedza(napis.val, kopia.val) is True):
            napis.next=kopia
            prev.next=napis
            return True
        prev=kopia
        kopia=kopia.next
    return False

zbior=utworz_linkliste_z_listy(["bartek", "leszek", "marek", "zosia"])
kopia=zbior
while kopia.next is not None:
    kopia=kopia.next
kopia.next=zbior
napis=Node("ola")
if(f(zbior, napis) is True):
    zbior=napis
wypisz(zbior)

