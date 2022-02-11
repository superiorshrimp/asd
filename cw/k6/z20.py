'''
Zadanie 18. W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
(np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
narożnika
!!!z dowolnego na dowolne!!!
'''
import random
import math

def pierwsza_cyfra(n):
    dl=math.floor(math.log10(n))
    w=n//10**(dl)
    return w

def dystans(w, k, cel_w, cel_k, nowe_w, nowe_k):
    d1=(w-cel_w)**2+(k-cel_k)**2
    d2=(nowe_w-cel_w)**2+(nowe_k-cel_k)**2
    if(d1<d2):
        return False
    return True

def czy_mozna(nowe_w, nowe_k, q):
    global T
    if(pierwsza_cyfra(T[nowe_w][nowe_k])==q):
        return True
    return False

def czy_nalezy(w, k, ruch):
    global T
    if(w+ruch[0]<0 or w+ruch[0]==len(T) or k+ruch[1]<0 or k+ruch[1]==len(T)):
        return False
    return True

def f(w, k, cel_w, cel_k):
    
    if(w==cel_w and k==cel_k):
        print("tak")
        exit(0)
        return
    global T
    q=T[w][k]%10
    global ruchy
    for ruch in ruchy:
        if(czy_nalezy(w, k, ruch)==True and dystans(w, k, cel_w, cel_k, w+ruch[0], k+ruch[1])==True and czy_mozna(w+ruch[0], k+ruch[1], q)==True):
            f(w+ruch[0], k+ruch[1], cel_w, cel_k)
    print("nie")
    exit(0)
    return

ruchy=((1,1), (1,-1), (-1,1), (-1,-1), (0,1), (1,0), (-1,0), (0,-1))
T=[[random.randint(1,100) for j in range(8)] for i in range(8)]
#T=[[2 for j in range(8)] for i in range(8)]
for i in range(len(T)):
    print(T[i])
print(f(1, 1, 3, 3))
#nie dziala ale blisko