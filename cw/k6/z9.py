'''
Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.
Zadanie 8. Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach
Zadanie 9. Poprzednie zadanie. Program powinien wypisywać wybrane odważniki.
'''
def f(T, n, i, P):
    if(i==len(T)):
        return False
    if(n==0):
        print(P)
        return True
    return f(T, n, i+1, P+[T[i]]) or f(T, n-T[i], i+1, P) or f(T, n+T[i], i+1, P+[-T[i]])


T=[5, 2, 33]
n=3
print(f(T, n, 0, []))
