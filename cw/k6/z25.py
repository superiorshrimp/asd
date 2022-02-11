'''
Zadanie 25. Tablica t[N] jest wypełniona liczbami naturalnymi. Skok z pola i-tego można wykonać na pola
o indeksach i+k, gdzie k jest czynnikiem pierwszym liczby t[i] (mniejszym od niej samej). Napisz funkcję,
która sprawdza, czy da się przejść z pola 0 do N-1 – jeśli się da, zwraca ilość skoków, jeśli się nie da, zwraca
-1.
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
        return [n]
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
print(f(T, 0))
print(licznik)