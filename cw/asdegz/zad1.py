#Szymon Żychowicz
'''
algorytm opiera się na łączeniu serii naturalnych
k = maksimum z inwersji dla każdego elementu wejściowej tablicy
wykorzystanie serii naturalnych pozwala uzyskać złożoność na poziomie O(nlogn) zamiast O(n^2) jak w przypadku bubble sorta czy quicksorta i porównywania pozycji dla niefortunnych danych 
'''

from zad1testy import runtests

class PQ:
    def __init__(self, val, maks):
        self.val=val
        self.maks=maks
    def __gt__(self, other):
        return self.val>other.val
    def __ge__(self, other):
        return self.val>=other.val
    def __eq__(self, other):
        return self.val==other.val
    def __le__(self, other):
        return self.val<=other.val
    def __lt__(self, other):
        return self.val<other.val

def find(t1, t2):
    if len(t2)==0:
        return 0
    a, b = t1[len(t1)-1], t2[0]
    l, p = 0, 0
    for i in range(len(t2)):
        if a>t2[i]:
            l+=1
        else:
            break
    for j in range(len(t1)-1, -1, -1):
        if b<t1[j]:
            p+=1
        else:
            break
    q=max(l+t1[len(t1)-1].maks, p+t2[0].maks)
    t1[len(t1)-1].maks+=l
    t2[0].maks+=p
    return q

def merge_sorted_arrays(t1, t2): #łączy tablice t1 i t2 do tablicy T od indeksu k w T
    i, j = 0, 0
    T=[None for _ in range(len(t1)+len(t2))]
    maksimum=find(t1, t2)
    if len(t2)==0:
        return t1, maksimum
    while i<len(t1) and j<len(t2):
        if t1[i]<t2[j]:
            T[i+j]=t1[i]
            i+=1
        else:
            T[i+j]=t2[j]
            j+=1
    while i<len(t1):
        T[i+j]=t1[i]
        i+=1
    while j<len(t2):
        T[i+j]=t2[j]
        j+=1
    return T, maksimum

def chaos_index( T ):
    T=[PQ(T[i], 0) for i in range(len(T))]
    H=[]
    i=1
    start=0
    while i<len(T):
        if T[i]<T[i-1]:
            H.append(T[start:i])
            start=i
        i+=1
    H.append(T[start:i])
    if len(H)%2==1:
        H.append([])
    l=len(H)
    maksimum=0
    while True:
        for i in range(l//2):
            res=merge_sorted_arrays(H[2*i], H[2*i+1])
            H[i]=res[0]
            maksimum=max(maksimum, res[1])
        l//=2
        if l==1:
            break
        if l%2==1:
            H[l]=[]
            l+=1
    return maksimum

runtests( chaos_index )
