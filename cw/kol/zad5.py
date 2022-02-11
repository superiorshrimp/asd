#Szymon Żychowicz

'''
iteruje po kolejnych elementach az do przed przedostatniego i sprawdzam czy kolejny element lub pokolejny jest wzglednie pierwszy z poprzednimi
za pomoca funkcji pomocniczej
'''

def czy_wzglednie_pierwsze(a, b): #funkcja sprawdzajaca czy 2 liczby sa wzglednie pierwsze
    while(b!=0): #szukam nwd
            b, a = a%b, b
    if(a==1):
        return True
    return False

def trojki(T): #glowna funkcja
    if(len(T)<3): #jesli w tablicy nie ma nawet 3 elementow to od razu zwracam 0
        return 0
    licznik=0 #mam zwracac ilosc wiec ustawiam licznik
    for i in range(len(T)-2): #iteruje do len(T)-2, bo minimalna dlugosc ciagu szukanych liczb to 3
        a=T[i]
        if(czy_wzglednie_pierwsze(a, T[i+1])==True): #porownuje liczby
            b=T[i+1]
            if(czy_wzglednie_pierwsze(T[i+2], a)==True and czy_wzglednie_pierwsze(T[i+2], b)==True):
                licznik+=1
            if(i+3<len(T)): #sprawdzam czy nie wyszedlem za tablice; uważam, żeby nie dać elif
                if(czy_wzglednie_pierwsze(T[i+3], a)==True and czy_wzglednie_pierwsze(T[i+3], b)==True):
                    licznik+=1
        
        if(czy_wzglednie_pierwsze(a, T[i+2])==True):
            b=T[i+2]
            if(i+3<len(T)):
                if(czy_wzglednie_pierwsze(T[i+3], a)==True and czy_wzglednie_pierwsze(T[i+3], b)==True):
                    licznik+=1
            if(i+4<len(T)):
                if(czy_wzglednie_pierwsze(T[i+4], a)==True and czy_wzglednie_pierwsze(T[i+4], b)==True):
                    licznik+=1
    return licznik
