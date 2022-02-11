'''
import random

def partition(T, l, p):
    mid=(l+p)//2
    pivot=T[mid]
    i=l-1
    j=p+1
    while True:
        i+=1
        while T[i]<pivot:
            i+=1
        j-=1
        while T[j]>pivot:
            j-=1
        if i>=j:
            return j
        
        T[i], T[j] = T[j], T[i]


def quicksort(T, l, p):
    while l<p:
        q=partition(T, l, p)
        if abs(q-1-l)<abs(p-q+1):
            quicksort(T, l, q-1)
            l=q+1
        else:
            quicksort(T, q+1, p)
            p=q-1

T=[random.randint(0,10) for _ in range(10)]
quicksort(T, 0, len(T)-1)
print(T)
'''
'''
def heapify(T, i): #min
    l=2*i+1
    p=2*i+2
    if l<len(T):
        if p<len(T):
            if T[l][0]<T[p][0]:
                if T[l][0]<T[i][0]:
                    T[l], T[i] = T[i], T[l]
                    heapify(T, l)
            else:
                if T[p][0]<T[i][0]:
                    T[p], T[i] = T[i], T[p]
                    heapify(T, p)
        else:
            if T[l][0]<T[i][0]:
                T[l], T[i] = T[i], T[l]
                heapify(T, l)

def build_heap(T): #min
    for i in range(len(T)//2, -1, -1):
        heapify(T, i)


def merge_k_arrays(T): #T - liczba tablic (o łącznie n elementach)
    W=[]
    Tmp=[]
    for i in range(len(T)):
        Tmp.append((T[i][0], i, 0))
    build_heap(Tmp)
    while len(Tmp)!=0:
        value, tab_id, index = Tmp[0][0], Tmp[0][1], Tmp[0][2]
        W.append(value)
        if len(T[tab_id])>index+1:
            Tmp[0]=(T[tab_id][index+1], tab_id, index+1)
            heapify(Tmp, 0)
        else:
            if len(Tmp)>1:
                Tmp[0], Tmp[(len(Tmp)-1)] = Tmp[(len(Tmp)-1)], Tmp[0]
                del Tmp[len(Tmp)-1]
                heapify(Tmp, 0)
            else:
                del Tmp[0]
    return W

T=[
    [1,3,5,7,9],
    [2,4,6,8],
    [1,2,3],
    [1,8,9,11,12]
]
W=merge_k_arrays(T)
print(W)
'''
'''
def heapify_min(T, i, size):
    l=2*i+1
    p=2*i+2
    if(l<size):
        if(p<size):
            if(T[l]<=T[p]):
                if(T[i]>T[l]):
                    T[i], T[l] = T[l], T[i]
                    heapify_min(T, l, size)
            else:
                if(T[i]>T[p]):
                    T[i], T[p] = T[p], T[i]
                    heapify_min(T, p, size)
        else:
            if(T[i]>T[l]):
                T[i], T[l] = T[l], T[i]
                heapify_min(T, l, size)


def heapify_max(T, i, size):
    l=2*i+1
    p=2*i+2
    if(l<size):
        if(p<size):
            if(T[l]>=T[p]):
                if(T[i]<T[l]):
                    T[i], T[l] = T[l], T[i]
                    heapify_max(T, l, size)
            else:
                if(T[i]<T[p]):
                    T[i], T[p] = T[p], T[i]
                    heapify_max(T, p, size)
        else:
            if(T[i]<T[l]):
                T[i], T[l] = T[l], T[i]
                heapify_max(T, l, size)

def heap_insert_max(T, el):
    T.append(el)
    i=len(T)-1
    while (i-1)//2>=0:
        if(T[(i-1)//2]<T[i]):
            T[(i-1)//2], T[i] = T[i], T[(i-1)//2]
            i=(i-1)//2
        else:
            return

def heap_insert_min(T, el):
    T.append(el)
    i=len(T)-1
    while (i-1)//2>=0:
        if(T[(i-1)//2]>T[i]):
            T[(i-1)//2], T[i] = T[i], T[(i-1)//2]
            i=(i-1)//2
        else:
            return

def f(T): # zakladam ze dlugosc T jest wieksza bądź równa 3
    balance=0
    min_heap=[max(T[0], T[1])]
    max_heap=[min(T[0], T[1])]
    for i in range(2,len(T)):
        if T[i]>min_heap[0]:
            heap_insert_min(min_heap, T[i])
            balance=len(min_heap)-len(max_heap)
            if balance<-1:
                min_heap[0], min_heap[len(min_heap)-1] = min_heap[len(min_heap)-1], min_heap[0]
                heap_insert_max(max_heap, min_heap[len(min_heap)-1])
                del min_heap[len(min_heap)-1]
                heapify_min(min_heap, 0, len(min_heap))
        else:
            heap_insert_max(max_heap, T[i])
            balance=len(max_heap)-len(min_heap)
            if balance>1:
                max_heap[0], max_heap[len(max_heap)-1] = max_heap[len(max_heap)-1], max_heap[0]
                heap_insert_min(min_heap, max_heap[len(max_heap)-1])
                del max_heap[len(max_heap)-1]
                heapify_max(max_heap, 0, len(max_heap))
    if balance==-1: #wypisanie mediany
        return min_heap[0]
    elif balance==0:
        return (min_heap[0]+max_heap[0])/2
    else:
        return max_heap[0]

T=[5,6,8,9,11,2,3]
print(f(T))
'''
'''
def horae_partition(T, i, j):
    rem=j
    pivot=T[j]
    j-=1
    flag=0
    while j>i:
        if flag==1:
            T[i], T[j] = T[j], T[i]
        while T[i]<=pivot:
            i+=1
            flag=1
        while T[j]>pivot:
            j-=1
            flag=1
    T[i], T[rem] = pivot, T[i]
    return i
'''