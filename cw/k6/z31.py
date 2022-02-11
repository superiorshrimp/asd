'''
Zadanie 31. Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i
zwraca sumę iloczynów elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Można założyć,
że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym etapie funkcja powinna wpisać podzielniki do tablicy pomocniczej.
Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71
'''
def dzielniki_pierwsze(n):
    W=[]
    for i in range(2, int(n**(0.5))+1):
        if(n%i==0):
            W.append(i)
            while(n%i==0):
                n//=i
    return W

def f(T, s, i):
    global slownik
    slownik[s]=True
    if(i==len(T)):
        return None
    return f(T, s*T[i], i+1) or f(T, s, i+1)

slownik={}
#zakladam ze wybrana jest liczba zlozona
n=60
T=dzielniki_pierwsze(n)
f(T, 1, 0)
s=0
for key, value in slownik.items():
    s+=key
print(s-1)
#o 1 za duzo