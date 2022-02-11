'''
Zadanie 6. Liczby zespolone są reprezentowane przez krotkę (re, im). Gdzie: re - część rzeczywista liczby,
im - część urojona liczby. Proszę napisać podstawowe operacje na liczbach zespolonych, m.in. dodawanie,
odejmowanie, mnożenie, dzielenie, potęgowanie, wypisywanie i wczytywanie.
'''
T=[(7, 3), (-4, 11)]

def c_suma(T):
    s=(T[0][0]+T[1][0], T[0][1]+T[1][1])
    return s

def c_roznica(T):
    r=(T[0][0]-T[1][0], T[0][1]-T[1][1])
    return r

def iloczyn(T):
    i=(T[0][0]*T[1][0]-T[0][1]*T[1][1], T[0][1]*T[[1][0]+T[1][0]*T[0][1])
    return i

def iloraz(T):
    m=T[1][0]**2-T[1][1]**2
    l=iloczyn([T[0], ( T[1][0] , -T[1][1] )])
    return (l, m)

#iloraz cos zle

print(iloraz(T))