'''
Zadanie 3. Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
polu startowym i ostatnim także wliczamy do kosztu przejścia.
'''
'''
import random

def generowanie_dwuwymiarowej_tablicy():
    N=8
    T=[[random.randint(1, 100) for j in range(N)] for i in range(N)]
    for i in range(N):
        print(T[i][:])
    return T

def f(T, s, p, i):
    s+=T[i][p]
    global koszta
    if(i==7):
        if(s<koszta):
            koszta=s
        return
    if(p==0):
        return f(T, s, p, i+1) or f(T, s, p+1, i+1)
    elif(p==7):
        return f(T, s, p, i+1) or f(T, s, p-1, i+1)
    else:
        return f(T, s, p, i+1) or f(T, s, p+1, i+1) or f(T, s, p-1, i+1)

koszta=100*8+1
T=generowanie_dwuwymiarowej_tablicy()
for k in range(len(T)):
    f(T, T[0][k], k, 1)
print(koszta)
'''
import random

def generowanie_dwuwymiarowej_tablicy():
    N=8
    T=[[random.randint(1, 100) for j in range(N)] for i in range(N)]
    for i in range(N):
        print(T[i][:])
    return T

def f(T, k, i):
    if(k<0 or k>7):
        return 99999
    if(i==7):
        return T[i][k]
    return min(f(T, k-1, i+1), f(T, k+1, i+1), f(T, k, i+1))+T[i][k]

T=generowanie_dwuwymiarowej_tablicy()
min=9999999
for k in range(len(T)):
    a=f(T, k, 0)
    if(a<min):
        min=a
print(min)