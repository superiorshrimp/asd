#Szymon Żychowicz

def dlugosc(n): #dlugosc liczby (ilosc cyfr)
    dl=1
    while(n>=10):
        dl+=1
        n//=10
    return dl

def czy_pierwsza(n): #spr czy liczba jest pierwsza
    if(n==0 or n==1):
        return False
    for i in range(2, int(n**(0.5))+1):
        if(n%i==0):
            return False
    return True

def rek(n, w, i, podzialy, dl):
    q=(n//(10**(dl-i-1)))%10 #ita cyfra liczby (liczac od 0)
    if(i==podzialy): #warunek konca true
        return True
    if(czy_pierwsza(w)==True): #dla true sa 2 mozliwosci
        return rek(n, q*(10**(dl-i-1)), i+1, podzialy+1, dl) or rek(n, 10*w+q*(10**(dl-i-1)), i+1, podzialy, dl)
    if(i>dl): #warunek konca false
        return False
    return rek(n, 10*w+q*(10**(dl-i-1)), i+1, podzialy, dl) #sprawdzaj dalej

def divide(N):
    podzialy=[]
    dl=dlugosc(N)
    for i in range(2, dl+1):
        if(czy_pierwsza(i)==True):
            podzialy.append(i) #tworze mozliwe podzialy
    for k in podzialy:
        if(rek(N, 0, 0, k, dl)==True): #dla podzialow sprawdzam
            return True
    return False
