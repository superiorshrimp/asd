from math import log

def partition(T, l, p):
    pivot=T[0][p]
    j=l
    for i in range(l, p):
        if T[0][i]<=pivot:
            T[0][i], T[0][j] = T[0][j], T[0][i]
            j+=1
    T[0][p], T[0][j] = T[0][j], T[0][p]
    return j

def find_kth(T, l, p, k): #select
    q=partition(T, l, p)
    if q==k:
        return T[0][k]
    elif q<k:
        return find_kth(T, q+1, p, k)
    elif q>k:
        return find_kth(T, l, q-1, k)
    else:
        return None

def quicksort(T, l, p): #rekurencyjnie
    while l<p:
        q=partition(T, l, p)
        if abs(q-1-l)<abs(p-q+1):
            quicksort(T, l, q-1)
            l=q+1
        else:
            quicksort(T, q+1, p)
            p=q-1

def quick_search(T, n, l, p): #binary search
    left=l
    right=p
    while right-left>1:
        new=(left+right)//2
        if T[new]>n:
            right=new
        elif T[new]<n:
            left=new
        else:
            return new
    if T[left]==n:
        return left
    return None

def bonus(q, i):
    return max(0, 10-abs(q-i))

def stypendia(T, A, k):
    for j in range(len(T[0])):
        for i in range(1,len(T)):
            T[0][j]+=T[i][j]
    suma=T[0][A]
    a=0
    b=len(T[0])-1
    if len(T[0])//4-9>=0:
        a=find_kth(T, len(T[0])//4-9)
    if  len(T[0])//4+9<len(T[0]):
        b=find_kth(T, len(T[0])//4+9)
    quicksort(T, a, b)
    index=quick_search(T[0], suma, a, b)
    print(T[0], index,len(T[0])//4, bonus(len(T[0])//4, index))
    return suma+bonus(len(T[0])//4, index)>k
    
    

T = [[5.0, 5.0, 3.75, 4.5, 4.3, 4.1, 3.9, 4.9, 3.6, 2.0, 2.0, 2.0],
     [5.0, 4.6, 4.9, 4.2, 3.7, 4.0, 3.8, 4.01, 3.6, 3.5, 3.4, 2.0],
     [5.0, 4.7, 3.0, 3.5, 2.8, 2.7, 2.5, 2.0, 2.3, 2.2, 2.1, 2.4]]
F = [ [ T[i][j] for j in range(len(T[0]))] for i in range(len(T)) ]

print(stypendia(T,7,19) == True)
print(stypendia(F,7,21) == False)
#idk imo działa mimo widocznie polecenia nie rozumiem ale close enough