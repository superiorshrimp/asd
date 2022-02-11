from random import randint

def partition(T, l, p):
    pivot=T[p]
    j=l
    for i in range(l, p):
        if T[i]<=pivot:
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def quicksort(T, l, p): #rekurencyjnie
    while l<p:
        q=partition(T, l, p)
        if abs(q-1-l)<abs(p-q+1):
            quicksort(T, l, q-1)
            l=q+1
        else:
            quicksort(T, q+1, p)
            p=q-1

def quicksort_it(T, l, p): #iteracyjnie
    stack=[None for _ in range(len(T))]
    stack[0]=[l, p]
    top=0
    while top>=0:
        l, p = stack[top]
        top-=1
        q=partition(T, l, p)
        if q-1>l:
            top+=1
            stack[top]=[l, q-1]
        if q+1<p:
            top+=1
            stack[top]=[q+1, p]

def merge_sorted_arrays(T, t1, t2, k): #łączy tablice t1 i t2 do tablicy T od indeksu k w T
    i, j = 0, 0
    while i<len(t1) and j<len(t2):
        if t1[i]<t2[j]:
            T[k+i+j]=t1[i]
            i+=1
        else:
            T[k+i+j]=t2[j]
            j+=1
    while i<len(t1):
        T[k+i+j]=t1[i]
        i+=1
    while j<len(t2):
        T[k+i+j]=t2[j]
        j+=1

def merge_sort(T, t, k): #na start t=T, k=0
    if len(t)==1:
        return t
    t1=merge_sort(T, t[:len(t)//2], k)
    t2=merge_sort(T, t[len(t)//2:], k+len(t)//2)
    merge_sorted_arrays(T, t1, t2, k)
    return T[k:k+len(t)]

def bubble_sort(T):
    for i in range(len(T)):
        for j in range(len(T)-i-1):
            if T[j]>T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]

def insertion_sort(T):
    for i in range(1,len(T)):
        rem=T[i]
        j=i-1
        mem=T[i]
        while j>=0 and T[j]>rem:
            T[j+1]=T[j]
            j-=1
        T[j+1]=rem

def selection_sort(T):
    for i in range(len(T)-1):
        minimum=T[i]
        min_index=i
        for j in range(i+1, len(T)):
            if T[j]<minimum:
                minimum=T[j]
                min_index=j
        T[i], T[min_index] = T[min_index], T[i]

def heapify_max(T, i, size):
    l=2*i+1
    p=2*i+2
    maksimum=i
    if l<size and T[i]<T[l]:
        maksimum=l
    if p<size and T[maksimum]<T[p]:
        maksimum=p
    if maksimum!=i:
        T[i], T[maksimum] = T[maksimum], T[i]
        heapify_max(T, maksimum, size)

def heapify_min(T, i, size):
    l=2*i+1
    p=2*i+2
    minimum=i
    if l<size and T[i]>T[l]:
        minimum=l
    if p<size and T[minimum]>T[p]:
        minimum=p
    if minimum!=i:
        T[i], T[minimum] = T[minimum], T[i]
        heapify_min(T, minimum, size)

def build_heap(T):
    for i in range(len(T)//2, -1, -1):
        heapify_max(T, i, len(T))

def heapsort(T):
    build_heap(T)
    size=len(T)
    for i in range(len(T), 0, -1):
        T[0], T[i-1] = T[i-1], T[0]
        size-=1
        heapify_max(T, 0, size)

def counting_sort(T):
    A=[0 for _ in range(len(T))]
    for el in T:
        A[el]+=1
    for i in range(1,len(A)):
        A[i]+=A[i-1]
    W=[0 for _ in range(len(T))]
    for i in range(len(T)-1,-1,-1):
        A[T[i]]-=1
        W[A[T[i]]]=T[i]
    for i in range(len(W)):
        T[i]=W[i]

class Node:
    def __init__(self, val, next):
        self.val=val
        self.next=next

def insert(head, value):
    if value<head.val:
        new=Node(value, head)
        return new
    curr=head.next
    prev=head
    while curr is not None:
        if curr.val>value:
            new=Node(value, curr)
            prev.next=new
            break
        prev=curr
        curr=curr.next
    new=Node(value, curr)
    prev.next=new
    return head

def bucket_sort(T, start, stop): # liczby z zakresu [start, stop) w rozkładzie jednostajnym
    W=[None]*len(T)
    q=(stop-start)/len(T)
    for i in range(len(T)):
        id=int(T[i]/q)
        print(id)
        if W[id] is None:
            W[id]=Node(T[i], None)
        else:
            W[id]=insert(W[id], T[i])
    j=0
    for i in range(len(W)):
        while W[i] is not None:
            T[j]=W[i].val
            W[i]=W[i].next
            j+=1

def quick_search(T, n): #binary search
    left=0
    right=len(T)-1
    while right-left>1:
        new=(left+right)//2
        if T[new]>n:
            right=new
        elif T[new]<n:
            left=new
        else:
            break
    if T[left]==n:
        return left
    return None

def find_kth(T, l, p, k): #select
    q=partition(T, l, p)
    if q==k:
        return T[k]
    elif q<k:
        return find_kth(T, q+1, p, k)
    elif q>k:
        return find_kth(T, l, q-1, k)
    else:
        return None

def wartosc_wyrazu_leks(wyraz, baza, dl): #baza - wielkosc alfabetu (a,b,c - wielkosc to 3); uwaga: duze litery; dl - max dlugosc slowa
    i=dl-1 #leksykograficznie
    wartosc=0
    for litera in wyraz:
        wartosc+=(ord(litera)-97)*baza**i #ord("a")=97
        i-=1
    return wartosc

def wartosc_wyrazu(wyraz, baza): #baza - wielkosc alfabetu
    i=len(wyraz)-1 #nie leksykograficznie
    wartosc=0
    for litera in wyraz:
        wartosc+=(ord(litera)-97)*baza**i #ord("a")=97
        i-=1
    return wartosc
