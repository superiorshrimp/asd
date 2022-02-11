'''
Zadanie 4. Dana jest tablica zawierająca liczby wymierne. Proszę napisać funkcję, która policzy występujące w tablicy ciągi arytmetyczne (LA) i geometryczne (LG) o długości większej niż 2. Funkcja powinna
zwrócić wartość 1 gdy LA > LG, wartość -1 gdy LA < LG oraz 0 gdy LA = LG
'''
import random
T=[(random.randint(1, 100), random.randint(1, 100)) for i in range(100)]

def skracanie(l, m):
    if(l==0):
        return (0, 1)
    if(l*m<0):
        l, m = abs(l), abs(m)
        z=-1
    else:
        z=1
    D=[[1], [1]]
    for i in range(1, l//2+1):
        if(l%i==0):
            D[0].append(i)
    for i in range(1, m//2+1):
        if(m%i==0):
            D[1].append(i)
    for k in D[0][::-1]:
        if k in D[1]:
            l//=k
            m//=k
            if(z==-1):
                l*=-1
            return (l, m)

def roznica(a, b):
    m=a[1]*b[1]
    l=a[0]*b[1]-b[0]*a[1]
    w=skracanie(l, m)
    return w

def iloraz(a, b):
    l=a[0]*b[1]
    m=a[1]*b[0]
    w=skracanie(l, m)
    return w

def f(T):
    N=len(T)
    licznikr=0
    licznikq=0
    maxr=0
    maxq=0
    for i in range(N-1):
        r=roznica(T[i+1], T[i])
        q=iloraz(T[i+1], T[i])
        k=2
        l=2
        while(i+k<N):
            if(roznica(T[i+k], T[i+k-1])==r):
                licznikr+=1
                if(licznikr>maxr):
                    maxr=licznikr
                else:
                    k+=N
            k+=1
        while(i+l<N):
            if(iloraz(T[i+l], T[i+l-1])==q):
                licznikq+=1
                if(licznikq>maxq):
                    maxq=licznikq
                else:
                    l+=N
    return maxr, maxq

print(f(T))

#cos nie dziala