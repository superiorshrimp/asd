'''
Zadanie 1. Liczby wymierne są reprezentowane przez krotkę (l,m). Gdzie: l - liczba całkowita oznaczająca
licznik, m - liczba naturalna oznaczająca mianownik. Proszę napisać podstawowe operacje na ułamkach,
m.in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, skracanie, wypisywanie i wczytywanie
'''
l, m, k, n = -2, 8, 3, 16
T=[(l, m), (k, n)]

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

def skr(l, m):
    def nwd(l, m):
        while(m!=0):
            l, m = l, l%m
        return l
    return l//nwd(l, m), m//nwd(l, m)

def suma(T):
    m=T[0][1]*T[1][1]
    l=T[0][0]*T[1][1]+T[1][0]*T[0][1]
    print(l, m)
    w=skracanie(l, m)
    return w

def roznica(T):
    m=T[0][1]*T[1][1]
    l=T[0][0]*T[1][1]-T[1][0]*T[0][1]
    print(l, m)
    w=skracanie(l, m)
    return w

def iloczyn(T):
    l=T[0][0]*T[1][0]
    m=T[0][1]*T[1][1]
    w=skracanie(l, m)
    return w

def iloraz(T):
    l=T[0][0]*T[1][1]
    m=T[0][1]*T[1][0]
    w=skracanie(l, m)
    return w

def potega(T):
    skr(T[1][0], T[1][1])
    skr(T[0][0], T[0][1])
    return (T[0][0]**T[1][0]**(iloraz([(1, 1), T[1]])), T[0][1]**T[1][0]**(iloraz([(1, 1), T[1]])))
#pot zle
print(potega(T))