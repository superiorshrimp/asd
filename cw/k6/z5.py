'''
Zadanie 5. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
110100 nie jest możliwe.
'''
import random
import math

def zamiana_na_dziesietny(n, dl):
    w=0
    for i in range(dl):
        w+=(n%10)*2**i
        n//=10
    return w

def czy_pierwsza(n):
    if(n==1 or n==0):
        return False
    for i in range(2, int(n**(0.5))+1):
        if(n%i==0):
            return False
    return True

def f(n, w, dl, i, dln):
    wd=zamiana_na_dziesietny(w, dl)
    if(i==dln and czy_pierwsza(wd)==True):
        return True
    if(dl>30):
        return None
    nowe=(n//(10**(dl-i)))%10
    if(czy_pierwsza(wd)==True and nowe==1):
        return f(n, 1, 1, i+1, dln) or f(n, 10*w+nowe, dl+1, i+1, dln)
    else:
        return f(n, 10*w+nowe, dl+1, i+1, dln)

'''
n=0
for i in range(100):
    n=n*10+random.randint(0, 1)
'''

n=110100
dl=math.floor(math.log10(n)+1)
print(f(n, 0, 0, 0, dl))
