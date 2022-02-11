'''
Zadanie 2. ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.
'''
'''
#3 spojne podzbiory
def waga(n):
    licznik=0
    if(n==1):
        return 0
    i=2
    while(n!=1):
        if(n%i==0):
            licznik+=1
            n//=i
            while(n%i==0):
                n//=i
        i+=1
    return licznik

def rek(T, s1, s2, l, p, suma):
    if(s1==s2==suma):
        return True
    if(l==p or l==p+1 or s1>suma or s2>suma):
        return False
    return rek(T, s1+T[l], s2, l+1, p, suma) or rek(T, s1, s2+T[p], l, p-1, suma)

def f(T):
    suma=0
    for i in range(len(T)):
        T[i]=waga(T[i])
        suma+=T[i]
    if(suma%3!=0 and suma!=0):
        return False
    return rek(T, 0, 0, 0, len(T)-1, suma//3)

T=[16, 4, 8, 14, 7]
print(f(T))
'''
#3 podzb
def waga(n):
    licznik=0
    if(n==1):
        return 0
    i=2
    while(n!=1):
        if(n%i==0):
            licznik+=1
            n//=i
            while(n%i==0):
                n//=i
        i+=1
    return licznik

def rek(T, s1, s2, s3, suma, i):
    if(s1==s2==s3==suma//3):
        return True
    if(i==len(T)):
        return False
    if(s1>suma//3 or s2>suma//3 or s3>suma//3):
        return False
    return rek(T, s1+T[i], s2, s3, suma, i+1) or rek(T, s1, s2+T[i], s3, suma, i+1) or rek(T, s1, s2, s3+T[i], suma, i+1)


def f(T):
    suma=0
    for i in range(len(T)):
        T[i]=waga(T[i])
        suma+=T[i]
    if(suma%3!=0 and suma!=0):
        return False
    return rek(T, 0,0,0,suma,0)

T=[16, 4, 8, 14, 7]
print(f(T))