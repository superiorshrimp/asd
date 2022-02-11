'''
Zadanie 13. Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników. Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.
'''
'''
def f(n, w, i, T):
    if(i==n):
        return None
    if(w==n):
        print(T)
        return None
    if(w>n):
        return False
    return f(n, w+i, i, T+[i]) or f(n, w, i+1, T) or f(n, w+i, i+1, T+[i])
T=[]
n=4
print(f(n, 0, 1, T))
'''
'''
Zadanie 13. Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników. Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.
'''
def rek(n, suma, i, skladniki):
    if(n==suma):
        print(skladniki)
        return
    if(suma>n or i==n):
        return
    rek(n, suma, i+1, skladniki)
    rek(n, suma+i, i, skladniki+[i])

def f(n):
    rek(n, 0, 1, [])
    return

f(4)