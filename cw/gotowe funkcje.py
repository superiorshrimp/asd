
def generowanie_dwuwymiarowej_tablicy():
    import random
    N=10
    T=[[random.randint(1, 10) for j in range(N)] for i in range(N)]
    for i in range(N):
        print(T[i][:])
    return T

def generowanie_jednowymiarowej_tablicy():
    import random
    N=1000
    T=[random.randint(1, 1000) for i in range(N)]
    return T

def kopia_jednowymiarowej_tablicy(T1):
    T2=[T1[i] for i in range(len(T1))]
    return T2

def kopia_dwuwymiarowej_tablicy(T1):
    T2=[[T1[i][j] for j in range(len(T1))] for i in range(len(T1))]
    return T2
    
def zamiana_na_binarny(n):
    W=[]
    while(n!=0):
        W.append(n%2)
        n//=2
    liczba=0
    for k in W[::-1]:
        liczba=10*liczba+k
    return liczba
    '''
def zamiana_na_binarny(n, licznik):
    W=[0]*licznik
    i=0
    while(n!=0):
        W[i]=n%2
        n//=2
        i+=1
    liczba=0
    for k in W[::-1]:
        liczba=10*liczba+k
    return liczba
n=17
p=n
licznik=0
while(p!=0):
    p//=2
    licznik+=1
print(licznik, zamiana_na_binarny(n, licznik))
'''

def zamiana_na_dowolny_system(n, i):
    key="0123456789ABCDEF"
    w=""
    while(n!=0):
        w+=key[n%i]
        n//=i
    w=w[::-1]
    return w
    
def rewers(n):
    rewers=0
    while(n!=0):
        rewers=10*rewers+n%10
        n//=10
    return rewers

def nwd(a, b):
    while(b!=0):
        b, a = a%b, b
    return a
#uwaga na wartosci ujemne

def czy_pierwsza(n):
    if(n==0 or n==1):
        return False
    for i in range(2, int(n**(0.5))+1):
        if(n%i==0):
            return False
    return True

def czy_wzglednie_pierwsze(a, b):
    while(b!=0):
            b, a = a%b, b
    if(a==1):
        return True
    return False

def dzielenie_w_slupku(a, b):
    w=str(a//b)+"."
    l=a
    p=(a//b)*b
    while(len(w)!=10):
        w+=str(l//b)
        l=10*(l-p)
        p=(l//b)*b
    return w

def singletony(T):
    P=[]
    i=0
    while(i<len(T)):
        k=T[i]
        T.remove(k)
        P.append(k)
        if k in T:
            P.remove(k)
            while k in T:
                T.remove(k)
    return P

def zbior(T):
    P=[]
    for k in T:
        if k not in P:
            P.append(k)
    return P

def sortowanie_qs(T):
    mniejsze=[]
    rowne=[]
    wieksze=[]
    if(len(T)>1):
        n = T[0]
        for k in T:
            if(k>n):
                wieksze.append(k)
            elif(k<n):
                mniejsze.append(k)
            else:
                rowne.append(k)
        return sortowanie(mniejsze)+rowne+sortowanie(wieksze)
    else:
        return T

def wykreslanie_itej_cyfry_z_liczby_o_dlugosci_dl(w, i, dl):
    q=(w//(10**(dl-i-1)))%10 #ita cyfra
    return q*(10**(dl-i-1))

def dlugosc(n):
    dl=1
    while(n>=10):
        dl+=1
        n//=10
    return dl

def waga(n): #ilosc roznych dzielnikow pierwszych
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

def zamiana_na_dziesietny(n, dl):
    w=0
    for i in range(dl):
        w+=(n%10)*2**i
        n//=10
    return w

def czy_mozna_hetmani(T, y, x):
    for i in range(len(T)):
        if(i!=y and T[i][x]==1):
            return False
    for j in range(len(T)):
        if(j!=x and T[y][j]==1):
            return False
    i, j = 1, 1
    while(x-j>=0 and y-i>=0):
        if(T[y-i][x-j]==1):
            return False
        i+=1
        j+=1
    i, j = 1, 1
    while(x+j<len(T) and y+i<len(T)):
        if(T[y+i][x+j]==1):
            return False
        i+=1
        j+=1
    return True

def pierwsza_cyfra(n):
    dl=dlugosc(n)
    return n//10**(dl-1)

