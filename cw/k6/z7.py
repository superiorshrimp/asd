'''
Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.
'''

T=[3, 5]
n=7

def f(T, n, i):
    if(n==0):
        return True
    elif(n<0):
        return False
    elif(i==len(T)):
        return False
    return f(T, n, i+1) or f(T, n-T[i], i+1)

print(f(T, n, 0))