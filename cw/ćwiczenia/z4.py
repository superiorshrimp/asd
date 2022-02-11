''' #sortowanie n liczb o wartosciach od 0 do n^2 w czasie liniowym - zamiana systemu liczbowego i radix sort
import datetime
import random
tp=datetime.datetime.now()

def sortuj(T):
    W=f(T, 1)
    return f(W, len(T))

def f(T, step):
    W=[0]*len(T)
    Count=[0]*len(T)
    for i in range(len(T)): #O(n)
        Count[(T[i]//step) % len(T)]+=1
    for i in range(1,len(T)): #O(n)
        Count[i]+=Count[i-1]
    for i in range(len(T)-1, -1, -1): #O(n)
        Count[(T[i]//step) % len(T)]-=1
        id=Count[(T[i]//step) % len(T)]
        W[id]=T[i]
    return W


for i in range(100):
    T=[random.randint(0,9999) for _ in range(100)]
    sortuj(T)

tk=datetime.datetime.now()
print("czas: ", tk-tp)
'''
'''
# tablica dlugosci n zawierajaca sufit logn roznych wartosci Sz: najszybsze sortowanie
def insert(T, val, l):
    p=len(T)-1
    T.append([val, 1])
    while p>=l:
        T[p+1], T[p] = T[p], T[p+1]
        p-=1
    T[l]=[val, 1]
    return

def binary_search(T, val): #na krotkach (value, count)
    if len(T)==0:
        T.append([val, 1])
        return
    l=0
    p=len(T)-1
    while l<p:
        mid=(l+p)//2
        if T[mid][0]>val:
            p=mid-1
        elif T[mid][0]<val:
            l=mid+1
        else:
            T[mid][1]+=1
            return
    q=T[l][0]
    if q==val:
        T[l][1]+=1
    elif val>q:
        insert(T, val, l+1)
    else:
        insert(T, val, l)

def binary_search_odejmowanie(T, val):
    l=0
    p=len(T)-1
    while l<p:
        mid=(l+p)//2
        if T[mid][0]>val:
            p=mid-1
        elif T[mid][0]<val:
            l=mid+1
        else:
            T[mid][1]-=1
            return mid
    T[l][1]-=1
    return l

def f(T):
    Count=[]
    for i in range(len(T)):
        binary_search(Count, T[i])
    for i in range(1,len(Count)):
        Count[i][1]+=Count[i-1][1]
    W=[0]*len(T)
    for i in range(len(T)-1, -1, -1):
        id=binary_search_odejmowanie(Count, T[i])
        W[Count[id][1]]=T[i]
    return W

T=[1,3,2,4,2,2,2,3,1,4,1,2,1,4,2,1]
print(f(T))
'''
'''
from random import randint

def partition(T, l, p): # normalne partition
    pivot=T[p]
    j=l
    for i in range(l, p):
        if(T[i]<=pivot):
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def median(T, l, p, k): # zwraca rekurencyjnie mediane (lewą) liczb od l do p 
    q=partition(T, l, p)
    if q==k:
        return T[q]
    elif q>k:
        return median(T, l, q-1, k)
    else:
        return median(T, q+1, p, k)

def mag5(T, l, p): # zwraca rekurencyjnie medianę median - nasz piwot
    if l==p:
        return T[l]
    rem=l
    while p-l>=5:
        val = median(T, l, l+4, l+2)
        T[l+2], T[rem+(l-rem)//5] = T[rem+(l-rem)//5], val
        l+=5
    if l<p:
        val = median(T, l, p, (l+p)//2)
        T[(l+p)//2], T[rem+(l-rem)//5] = T[rem+(l-rem)//5], val
        return mag5(T, rem, rem+(l-rem)//5)
    else:
        return mag5(T, rem, rem+(l-rem)//5-1)
    
def bigger_partition(T, l, p): # liczby sie nie powtarzaja
    pivot=mag5(T, l, p)
    j=l
    for i in range(l, p+1):
        if T[i]<pivot:
            T[i], T[j] = T[j], T[i]
            j+=1
        elif T[i]==pivot:
            T[i], T[j] = T[j], T[i]
            rem=j
            j+=1
    T[rem], T[j-1] = T[j-1], T[rem]
    return j-1

def not_median(T, l, p, k):
    q=bigger_partition(T, l, p)
    if k<q:
        return not_median(T, l, q-1, k)
    elif k>q:
        return not_median(T, q+1, p, k)
    else:
        return T[k]

for _ in range(100):    
    T=[randint(0, 100) for _ in range(10)]
    w=not_median(T, 0, len(T)-1, 4)
    T=sorted(T)
    if T[4]!=w:
        print(T)
'''
'''
#zad7
def f(T, k):
    Count=[0]*k
    i=0
    licznik=0
    ilosc=0
    start=0
    min=len(T)
    min_start=-1
    min_stop=-1
    while i<len(T):
        print(Count, i, start, ilosc, licznik, min)
        ilosc+=1
        if Count[T[i]]==0:
            licznik+=1
        Count[T[i]]+=1
        if licznik==k:
            while start<=i:
                Count[T[start]]-=1
                ilosc-=1
                if Count[T[start]]==0:
                    licznik=k-1
                    start+=1
                    if ilosc+1<min:
                        min_start=start-1
                        min_stop=i
                        min=ilosc+1
                    break
                start+=1
        i+=1
    return min, min_start, min_stop

T=[1,2,1,0,1,4,3,1,2,4,3,2,1,1,0,0]
print(f(T, 5))
'''
'''
#zad4
from random import randint

def f(T, zakres): # zakres w poleceniu to 10**9 ale pamieci mi nie starcza; jednak mimo to jest wszystko dobrze, bo polecenie mowi ze jest duzo pamieci
    Count=[0]*zakres
    for i in range(len(T)):
        licznik=0
        for j in range(len(T[i])):
            if Count[T[i][j]]!=i:
                licznik+=1
                Count[T[i][j]]=i
        print(licznik)
    return

#T=[[randint(0,99) for j in range(randint(1,1000))] for i in range(100)]
#f(T, 1000)
'''
'''
def zad3a(wyraz1, wyraz2, k): # O(max(n, k))
    if len(wyraz1)==len(wyraz2):
        Count=[0]*k # O(k)
        for litera in wyraz1: # O(n)
            Count[ord(litera)-ord("a")]+=1
        for litera in wyraz2: # O(n)
            if Count[ord(litera)-ord("a")]==0:
                return False
            Count[ord(litera)-ord("a")]-=1
        return True
    else:
        return False

#print(zad3a("abca", "cbba", ord("z")-ord("a")))
'''