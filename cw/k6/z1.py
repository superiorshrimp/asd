'''
Zadanie 1. Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
cyfry. 
'''
'''
iteracyjnie chyba:
n=2315

def czy_pierwsza(n):
    for i in range(2, int(n**(0.5))+1):
        if(n%i==0):
            return False
    return True

def dlugosc(n):
    dl=1
    while(n>=10):
        dl+=1
        n//=10
    return dl

def rek(T, i):
    TC=[T[i] for i in range(len(T))]
    del TC[0]
    if(len(TC)>2):
        rek(TC, i)

def binarny(n):
    W=[]
    while(n!=0):
        W.append(n%2)
        n//=2
    licznik=0
    for k in W:
        if(k==1):
            licznik+=1
    return W, licznik

def silnia(n):
    a=1
    for i in range(1, n+1):
        a*=i
    return a

def f(n):
    dl=dlugosc(n)
    ile=1+dl+silnia(dl)//(silnia(dl-2)*silnia(2))
    for i in range(0, ile+1):
        a=str(n)
        w=""
        W, p=binarny(i)
        if(p>=2):
            for j in range(len(W)):
                if(W[j]==1):
                    w+=a[j]
            if(czy_pierwsza(int(w))==True):
                print(w)

f(n)
'''
'''
n="23158764"

def czy_pierwsza(n):
    for i in range(2, int(n**(0.5))+1):
        if(n%i==0):
            return False
    return True

def f(n, k, i):
    if(i==len(n)):
        return False
    if(len(k)>=2 and czy_pierwsza(int(k))==True and len(k)!=len(n)):
        print(k)
        return None
    return f(n, k+"", i+1) or f(n, k+n[i], i+1)

print(f(n, "" ,0))
'''
'''
#na intach
import math
def czy_pierwsza(n):
    if(n==0 or n==1):
        return False
    for i in range(2, int(n**(0.5))+1):
        if(n%i==0):
            return False
    return True

def f(n):
    global slownik
    if(n<10):
        return False
    for i in range(math.floor(math.log10(n))+1):
        right=n%(10**i)
        left=n//(10**(i+1))
        n1=left*(10**i)+right
        if(czy_pierwsza(n1)==True and n1>=10):
            slownik[n1]=True
        f(n1)
    return None
    
slownik={}  
f(2002)
for key, value in slownik.items():
    print(key)
'''
def czy_pierwsza(n):
    if(n==0 or n==1):
        return False
    for i in range(2, int(n**(0.5))+1):
        if(n%i==0):
            return False
    return True

def dlugosc(n):
    dl=1
    while(n>=10):
        dl+=1
        n//=10
    return dl

def wykr(w, i, dl):
    q=(w//(10**(dl-i-1)))%10
    return q*(10**(dl-i-1))

def rek(n, w, dl, i):
    if(dl<2):
        return
    if(czy_pierwsza(w)==True):
        global slownik
        slownik[w]=True
    if(i==dlugosc(n)):
        return    
    rek(n, w-wykr(w, i, dlugosc(n)), dl-1, i+1)
    rek(n, w, dl, i+1)

def f(n):
    global slownik
    rek(n, n, dlugosc(n), 0)
    for key, item in slownik.items():
        print(key)
slownik={}
f(1249)