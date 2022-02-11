'''
Zadanie 16. Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą liczbę samogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład 00ula00 → 117, 108, 97
oraz 00exe00 → 101, 120, 101. Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna wypisać
znaleziony wyraz.
'''
#a=97
#e=101
#i=105
#o-111
#u-117
#y-121

n, m, l, p = "cdef", "abgh", 0, 0
N, M = [], []
for i in range(len(n)):
    N.append(ord(n[i]))
    if(n[i]==97 or n[i]==101 or n[i]==105 or n[i]==111 or n[i]==117 or n[i]==121):
        l+=1
for i in range(len(m)):
    M.append(ord(m[i]))
    if(m[i]==97 or m[i]==101 or m[i]==105 or m[i]==111 or m[i]==117 or m[i]==121):
        p+=1
def wyraz(s1, s2):
    if(len(s1)==):
        
#jak na 2 arg???



wyraz(n, m)
