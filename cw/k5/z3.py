'''
Zadanie 3. Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N < 100). Położenie
hetmanów jest opisywane przez tablicę dane = [(w1, k1),(w2, k2),(w3, k3), ...(wN , kN )] Proszę napisać funkcję, która odpowiada na pytanie: czy żadne z dwa hetmany się nie szachują? Do funkcji należy przekazać
położenie hetmanów.
'''

import random
T=[[0 for j in range(100)] for i in range(100)]
#N=random.randint(2, 99)
N=15
H=[]
for i in range(N):
    a, b = random.randint(0, 99), random.randint(0, 99)
    if (a, b) not in H:
        H.append((a, b))
for k in H:
    T[k[0]][k[1]]=1
for k in H:
    n, m = 1, 1
    while(k[0]-n>=0 and k[1]-m>=0):
        if(T[k[0]-n][k[1]-m]==1):
            print("szachuja sie")
            exit(0)
        n+=1
        m+=1
    n, m = 1, 1
    while(k[0]-n>=0 and k[1]+m<=99):
        if(T[k[0]-n][k[1]-m]==1):
            print("szachuja sie")
            exit(0)
        n+=1
        m+=1
    n, m = 1, 1
    while(k[0]+n<=99 and k[1]-m>=0):
        if(T[k[0]-n][k[1]-m]==1):
            print("szachuja sie")
            exit(0)
        n+=1
        m+=1
    n, m = 1, 1
    while(k[0]+n<=99 and k[1]+m<=99):
        if(T[k[0]-n][k[1]-m]==1):
            print("szachuja sie")
            exit(0)
        n+=1
        m+=1
print("nie szachuja sie")
'''
'''
def h(H):
    for k in H:
        for l in H:
            if(l!=k):
                if(1.0==(k[0]-l[0])/(k[1]-l[1])):
                    return True
    return False
#^alternatywa


#
#
#hetman - królowa !!!!!!
#
#