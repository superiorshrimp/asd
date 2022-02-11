'''
Zadanie 26. Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr
1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość
wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
10010(2), 10100(2), 11000(2)
'''
import math

def czy_pierwsza(n):
    for i in range(2, int(n**(0.5))+1):
        if(n%i==0):
            return False
    return True

def f(a, b, w):
    global licznik
    if(a==0 and b==0):
        if(czy_pierwsza(w)==False):
            licznik+=1
        return None
    if(a==0):
        return f(a, b-1, w)
    if(b==0):
        return f(a-1, b, w+2**(a+b-1))
    return f(a-1, b, w+2**(a+b-1)) or f(a, b-1, w)

A=2
B=3
licznik=0
f(A-1, B, 2**(A+B-1))
print(licznik)