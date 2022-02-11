#Szymon Żychowicz
'''
można zauważyć, że wartości na głównej przekątnej to wartosci ktore w posortowanej tablicy stałyby na miejscach k1 do k2 (wzor jest w kodzie)
najpierw linearyzuję tablicę T (n^2)
potem szukam k1 i k2 (2*n^2)
następnie uzupełniam tablicę T aby spęłniała warunki zadania (n^2)
więc ostatecznie złożoność obliczeniowa to O(n^2)
używam O(n^2) dodatkowej pamięci 
'''
from zad1testy import runtests
def partition(T, l, p):
    pivot=T[p]
    j=l
    for i in range(l, p):
        if(T[i]<=pivot):
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def find_kth(T, l, p, k):
    q = partition(T, l, p)
    if q==k:
        return
    elif q<k:
        return find_kth(T, q+1, p, k)
    else:
        return find_kth(T, l, q-1, k)

def Median(T):
    N=len(T)
    Linear=[0]*N**2
    for i in range(len(T)):
        for j in range(len(T)):
            Linear[j*len(T)+i]=T[i][j]
    k1=len(T)**2//2-len(T)//2
    k2=len(T)**2//2+len(T)//2
    find_kth(Linear, 0, len(Linear)-1, k1)
    find_kth(Linear, k1, len(Linear)-1, k2)
    less=0
    more=k2
    for row in range(len(T)):
        for col in range(len(T)):
            if col==row:
                T[row][col]=Linear[k1+row]
            elif col<row:
                T[row][col]=Linear[less]
                less+=1
            else:
                T[row][col]=Linear[more]
                more+=1
    return T

runtests( Median )