def f(T): #O(n^3)
    for start in range(len(T)): #dla kazdego wierzcholka jako startu cyklu
        visited1=[0 for _ in range(len(T))] #odwiedzone pierwszego rzedu
        visited2=[-1 for _ in range(len(T))] #odwiedzone drugiego rzedu
        for el1 in T[start]: #dla kazdego sasiada
            visited1[el1]=1 #zaznaczenie ze jest sasiadem pierwszego rzedu
            for el2 in T[el1]: #dla kazdego jego sasiada
                if el2!=start and visited1[el2]==0: #jesli ten sasiad nie jest startowym ani nie jest pierwszego rzedu do startu
                    if visited2[el2]==-1: #jesli nie byl odwiedzony
                        visited2[el2]=el1 #to zaznaczam skad na niego przyszedlem 
                    else:
                        print(start, "-> ", el1, "-> ", el2,"-> ", visited2[el2]) #jesli byl odwiedzony to mozemy wypisac wynik
                        return True
    return False
T=[
    [1,4,5],
    [0,2],
    [1,3,6],
    [2,4,6],
    [0,3,6],
    [0,6],
    [2,3,4,5]
]

print(f(T))