'''
Zadanie 32. Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory o
jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.
'''

#T=[123, 6345, 4231, 9876765, 43, 5347, 8923754, 1, 2, 238947, 3457]

def f(T, k, sl, sp, kl, kp, i):
    if(i==len(T)):
        return False
    if(kl>k or kp>k):
        return False
    if(kl==k and kp==k and sl==sp):
        print(sl)
        return True
    return f(T, k, sl+T[i], sp, kl+1, kp, i+1) or f(T, k, sl, sp+T[i], kl, kp+1, i+1) or f(T, k, sl, sp, kl, kp, i+1)

k=3
T=[2, 5, 6, 45, 234, 9, 32, 45, 3]
print(f(T, k, 0, 0, 0, 0, 0))  