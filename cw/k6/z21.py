'''
Zadanie 21. Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
wartość sumy, funkcja powinna zwrócić wartość typu bool.
'''
import random

def czy_mozna(i, k, tw, tk):
    if i not in tw and k not in tk:
        return True
    return False


def f(T, suma, i, tw, tk):
    print(suma)
    if(suma==0 and len(tw)>0):
        print("tag")
        return True
    if(suma<0):
        return
    if(i==len(T)):
        return
    for k in range(len(T)):
        if(czy_mozna(i, k, tw, tk)==True):
            f(T, suma-T[i][k], i+1, tw+[i], tk+[k])
        f(T, suma, i+1, tw, tk)
T=[
    [1,2,3],
    [4,5,6],
    [7,8,100]
]
#T=[[random.randint(1,10) for j in range(4)] for i in range(4)]

print(f(T, 101 , 0, [], []))