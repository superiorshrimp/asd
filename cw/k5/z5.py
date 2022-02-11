'''
Zadanie 5. Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy struktury dane =
[(x1, y1),(x2, y2),(x3, y3), ...(xN , yN )] Proszę napisać funkcję, która zwraca wartość True jeżeli zbiorze istnieją 4 punkty wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, a wewnątrz
tego kwadratu nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie
punktów
'''
import random
A=[0 for i in range(1000)]
for i in range(1000):
    x=random.randint(0, 49)
    y=random.randint(0, 49)
    while (x, y) in A:
        x=random.randint(0, 49)
        y=random.randint(0, 49)
    A[i]=(x, y)
print(A[:])
for d in range(1, len(A)):
    for k in A:
        if(k[0]+d<50 and k[1]+d<50):
            for l in A:
                if(l[0]==k[0]+d and l[1]==k[1]):
                    for i in A:
                        if(i[0]==k[0] and i[1]==k[1]+d):
                            for j in A:
                                if(j[0]==k[0]+d and j[1]==k[1]+d):
                                    print(d, k, l, i, j)
                                    exit(0)
                            
