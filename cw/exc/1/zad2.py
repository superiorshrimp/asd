#Szymon Żychowicz
'''
preprocessing: rekurencyjnie schodząc w dół drzewa tworzę tablicę w pole X o długości k+1 przechowywującą najdłuższe poddrzewa i<=k elementowe
działanie: rekurencyjnie schodzę w dół drzewa i z tamtąd wypełniam optymalnymi wynikami tablicę X
sa one optymalne, bo nowo powstałe drzewo jest spójne i wyniki od siebie nie zależą
dlaczego nowe drzewo jest spójne? bo zliczam poprzednie spójne poddrzewo plus krawędź je łączącą
złożoność: O(n*k**2)
'''
from zad2testy import runtests
from math import inf

class globe:
    def __init__(self, val):
        self.val=val

class Node:
    def __init__( self ):
        self.left    = None  # lewe podrzewo
        self.leftval = 0     # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right   = None  # prawe poddrzewo
        self.rightval= 0     # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X       = None  # miejsce na dodatkowe dane

def preprocessing(root, k):
    root.X=[None for _ in range(k+1)]
    root.X[0]=0
    if root.left is None:
        if root.right is None:
            return
        else:
            preprocessing(root.right, k)
    else:
        if root.right is None:
            preprocessing(root.left, k)
        else:
            preprocessing(root.left, k)
            preprocessing(root.right, k)

def rek(root, k, maksimum):
    if root.left is None and root.right is None:
        return root.X
    if root.left is not None:
        t1=rek(root.left, k, maksimum)
        if root.right is None:
            t2=[None for _ in range(k+1)]
        else:
            t2=rek(root.right, k, maksimum)
    else:
        t1=[None for _ in range(k+1)]
        t2=rek(root.right, k, maksimum)
    T=root.X
    #TODO: zmienic na while; brak czasu ale od wystąpienia pierwszego None nie trzeba dalej sprawdzac forem
    for i in range(k):
        if t1[i] is not None:
            T[i+1]=t1[i]+root.leftval
    for i in range(k):
        if t2[i] is not None:
            if T[i+1] is not None:
                T[i+1]=max(t2[i]+root.rightval, T[i+1])
            else:
                T[i+1]=t2[i]+root.rightval
    for i in range(k):
        for j in range(k):
            if t1[i] is not None and t2[j] is not None and i+j+2<=k:
                if T[i+j+2] is not None:
                    T[i+j+2]=max(T[i+j+2], root.leftval+root.rightval+t1[i]+t2[j])
                else:
                    T[i+j+2]=root.leftval+root.rightval+t1[i]+t2[j]
    if T[k] is not None:
        maksimum.val=max(maksimum.val, T[k])
    return T

      

def valuableTree( T, k ):
    preprocessing(T, k)
    maksimum=globe(-inf)
    rek(T, k, maksimum)
    return maksimum.val

runtests( valuableTree )