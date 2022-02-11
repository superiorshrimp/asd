'''
Zadanie 6. Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
Na przykład dla tablicy: [1,7,3,5,11,2] rozwiązaniem jest liczba 10.
'''
import random

def f(T, s, si, dl, i):
    if(s==si and dl!=0):
        global suma
        if(suma[1]<dl):
            suma[1]=dl
            suma[0]=s
        return dl
    if(i==len(T)):
        return len(T)+1
    return min(f(T, s+T[i], si+i, dl+1, i+1), f(T, 0, 0, 0, i+1), f(T, s, si, dl, i+1))

#T=[random.randint(1, 100) for i in range(100)]
suma=[0, 0]
T=[1,7,3,5,11,2]
#T=[1, 0, 2]

print(f(T, 0, 0, 0, 0))
print(suma[0])