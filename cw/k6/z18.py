'''
Zadanie 18. W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
(np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
narożnika.
'''
import math
import random
def pierwsza_cyfra(n):
    dl=math.floor(math.log10(n))
    return n//10**(dl)

def f(w, k):
    if(w==7 and k==7):
        print("tak")
        exit(0)
    global T
    a=T[w][k]%10
    if(w<7 and k<7):
        if(a<pierwsza_cyfra(T[w+1][k])):
            f(w+1, k)
        if(a<pierwsza_cyfra(T[w+1][k+1])):
            f(w+1, k+1)
        if(a<pierwsza_cyfra(T[w][k+1])):
            f(w, k+1)
    if(w==7):
        if(a<pierwsza_cyfra(T[w][k+1])):
            f(w, k+1)
    if(k==7):
        if(a<pierwsza_cyfra(T[w+1][k])):
            f(w+1, k)

T = [
 [1,4,6,2,3,5,35,2],
 [1,4,6,2,3,5,35,2],
 [1,4,6,82,3,5,35,2],
 [1,4,6,2,3,5,35,2],
 [1,4,6,2,3,5,91,2],
 [1,4,6,82,3,5,24,2],
 [1,4,6,2,3,5,35,7],
 [1,4,6,2,3,5,35,8],
]
#=[[random.randint(1, 16) for _ in range(8)] for _ in range(8)]
for i in range(8):
    print(T[i][:])
#T=[[1 for _ in range(8)] for _ in range(8)]
f(0, 0)

