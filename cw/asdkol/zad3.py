#Szymon Żychowicz
'''
złożoność O(nlogn)
użyłem quicksorta, bo wyznaczenie takich przedziałów w których już żadne 2 na siebie nie nachodzą,
aby zastosować bucketsort na optymalnych kubełkach, wymagałoby ich posortowania (no niby można niesortować, ale wtedy złożoność ułożenia odpowiednich przedziałów to n^2) co samo w sobie ma złożoność O(nlogn),
co sprawi, że taki kod asymptotycznie wcale nie byłby lepszy
złożoność pamięciowa mojego rozwiązania to O(logn) dodatkowej pamięci
'''

from zad3testy import runtests

def partition(T, l, p):
    pivot=T[p]
    j=l
    for i in range(l, p):
        if(T[i]<=pivot):
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def quicksort(T, l, p): #max logn dodatkowej pamięci
    while l<p:
        q=partition(T, l, p)
        if abs(q-1-l)<abs(p-q+1):
            quicksort(T, l, q-1)
            l=q+1
        else:
            quicksort(T, q+1, p)
            p=q-1

def SortTab(T,P):
    return quicksort(T, 0, len(T)-1)
    

runtests( SortTab )