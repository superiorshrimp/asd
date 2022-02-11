'''
Zadanie 22. Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację czy jest
możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe
'''
def dzielniki_pierwsze(n):
    if(n==0 or n==1):
        return [0]
    W=[]
    for i in range(2, n//2+1):
        if(n%i==0):
            W.append(i)
            while(n%i==0):
                n//=i
    if(len(W)==0):
        return [0]
    return W

def f(T, i):
    global licznik
    licznik+=1
    W=dzielniki_pierwsze(T[i])
    if(i==len(T)-1):
        return True
    if(W[0]==0):
        licznik=0
        return False    
    if(i>len(T)-1):
        return None
    for k in W:
        return f(T, i+k)

T=[15, 2, 3, 4, 7, 3]
licznik=0
if(f(T, 0)==True):
    print(licznik)
else:
    print(False)