'''
10. Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać
funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna
powstać nowa lista. 
'''
class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

def dodaj(liczba, cyfra): #zakladam ze dodawane sa cyfry i pierwsza nie jest 0
    if(liczba==None):
        liczba=Node(cyfra)
        return liczba
    prev=liczba
    kopia=liczba.next
    while(kopia!=None):
        prev=kopia
        kopia=kopia.next
    kopia=Node(cyfra)
    prev.next=kopia
    return liczba
    
def wypisz(liczba):
    while(liczba!=None):
        print(liczba.val, end=" ")
        liczba=liczba.next
    print()
    return

def dodawanie(liczba1, liczba2, i):
    nowa=None
    while(i>0):
        nowa=dodaj(nowa, liczba1.val)
        i-=1
        liczba1=liczba1.next
    while(liczba1!=None):
        nowa=dodaj(nowa, liczba1.val+liczba2.val)
        liczba1=liczba1.next
        liczba2=liczba2.next
    prev=nowa
    kopia=nowa.next
    while(kopia!=None):
        if(kopia.val>9):
            prev.val+=1
            kopia.val-=10
            kopia=nowa
        prev=kopia
        kopia=kopia.next
    wypisz(nowa)
    while(nowa.val>9):
        pom=(nowa.val-10)//10
        nowa.val=pom
        nowa=Node(pom+1, nowa)
    return nowa

def suma(liczba1, liczba2):
    nowa=None
    kopia1, kopia2 = liczba1, liczba2
    dl1, dl2 = 0, 0
    while(kopia1!=None):
        kopia1=kopia1.next
        dl1+=1
    while(kopia2!=None):
        kopia2=kopia2.next
        dl2+=1
    if(dl1>dl2):
        nowa=dodawanie(liczba1, liczba2, dl1-dl2)
    else:
        nowa=dodawanie(liczba2, liczba1, dl2-dl1)
    return nowa
    

liczba1, liczba2 = None, None
liczba1=dodaj(liczba1, 1)
liczba1=dodaj(liczba1, 2)
liczba1=dodaj(liczba1, 3)
liczba1=dodaj(liczba1, 1)
liczba1=dodaj(liczba1, 2)
liczba1=dodaj(liczba1, 3)
liczba1=dodaj(liczba1, 1)
liczba1=dodaj(liczba1, 2)
liczba1=dodaj(liczba1, 3)
liczba1=dodaj(liczba1, 1)
liczba1=dodaj(liczba1, 2)
liczba1=dodaj(liczba1, 3)
liczba2=dodaj(liczba2, 9)
liczba2=dodaj(liczba2, 9)
liczba2=dodaj(liczba2, 9)
liczba2=dodaj(liczba2, 9)
liczba2=dodaj(liczba2, 9)
liczba2=dodaj(liczba2, 9)
liczba2=dodaj(liczba2, 9)
liczba2=dodaj(liczba2, 9)
liczba2=dodaj(liczba2, 9)
liczba2=dodaj(liczba2, 9)
liczba2=dodaj(liczba2, 9)
liczba2=dodaj(liczba2, 9)
liczba2=dodaj(liczba2, 9)
liczba2=dodaj(liczba2, 9)
liczba2=dodaj(liczba2, 9)
liczba2=dodaj(liczba2, 9)
print(9999+123)
nowa=suma(liczba1, liczba2)
wypisz(nowa)
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
    while zbior is not None:
        print(zbior.val, end=" ")
        zbior=zbior.next
    print()
    return

def dodaj_jeden(zbior1, zbior2): #dodaje mniejsza
    curr1=zbior1 #789
    curr2=zbior2 #32
    while curr2 is not None:
        if(curr1.val+curr2.val>=10):
            if curr1.next is not None:
                curr1.next.val+=1
            else:
                nowy=Node(1)
                curr1.next=nowy
        curr1.val=(curr1.val+curr2.val)%10
        curr1=curr1.next
        curr2=curr2.next
    while curr1 is not None:
        if(curr1.val>=10):
            if curr1.next is not None:
                curr1.next.val+=1
            else:
                nowy=Node(1)
                curr1.next=nowy
        curr1=curr1.next
    return zbior1

wypisz(dodaj_jeden(utworz_linkliste_z_listy([7,8,9]), utworz_linkliste_z_listy([3,2])))
#poprawic
'''