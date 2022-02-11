'''
Zadanie 30. Punkt leżący na płaszczyźnie jest opisywany parą liczb typu float (x,y). Tablica T[N] zawiera
współrzędne N punktów leżących na płaszczyźnie. Punkty posiadają jednostkową masę. 
Proszę napisać funkcję, która sprawdza czy istnieje niepusty podzbiór n punktów, gdzie n¡k oraz n jest wielokrotnością liczby
3, którego środek ciężkości leży w odległości mniejszej niż r od początku układu współrzędnych. Do funkcji
należy przekazać dokładnie 3 parametry: tablicę t, promień r, oraz ograniczenie k, funkcja powinna zwrócić
wartość typu bool
'''

def rek(T, r, k, s, i, p):
    print(s)
    if(p!=0):
        if(s/p<r**2 and s!=0):
            if(p!=k and p%3==0):
                return False
            return True
    if(i==len(T)):
        return False
    return rek(T, r, k, s, i+1, p) or rek(T, r, k, s+T[i][0]**2+T[i][1]**2, i+1, p+1)

def f(T, r, k):
    return rek(T, r, k, 0, 0, 0)

T=[(21, 37), (-14, 88), (0, -20), (1, 1), (3, 3), (-3, -3)]
r=3
k=2

print(f(T, r, k))