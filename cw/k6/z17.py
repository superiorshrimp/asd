'''
Zadanie 17. Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
zadanych liczb.
'''
def dlugosc(n):
    licznik=1
    while(n>=10):
        licznik+=1
        n//=10
    return licznik

def ita_cyfra(n, dl, i):
    return (n//(10**(dl-i)))%10 

def czy_pierwsza(n):
    if(n==0 or n==1):
        return False
    for i in range(2, int(n**(0.5))+1):
        if(n%i==0):
            return False
    return True

def rek(w, l, p, l_index, p_index):
    if(l_index==dlugosc(l)+1 and p_index==dlugosc(p)+1):
        print(w, czy_pierwsza(w))
        if(czy_pierwsza(w)==True):
            global licznik
            licznik+=1
        return
    if(l_index<dlugosc(l)+1):
        rek(10*w+ita_cyfra(l, dlugosc(l), l_index), l, p, l_index+1, p_index)
    if(p_index<dlugosc(p)+1):
        rek(10*w+ita_cyfra(p, dlugosc(p), p_index), l, p, l_index, p_index+1)
    return
    
def f(l, p):
    rek(0, l, p, 1, 1)
    global licznik
    return licznik

licznik=0
print(f(1, 9))