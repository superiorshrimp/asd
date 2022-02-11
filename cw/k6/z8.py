'''
Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.
Zadanie 8. Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach
'''
T=[5, 2, 33]
n=17
def f(T, n, i):
    if(n==0):
        return True
    elif(i==len(T)):
        return False
    return f(T, n, i+1) or f(T, n-T[i], i+1) or f(T, n+T[i], i+1)

print(f(T, n, 0))