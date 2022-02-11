'''
Zadanie 2. Używając funkcji z poprzedniego zadania proszę napisać funkcję rozwiązującą układ 2 równań
o 2 niewiadomych.
'''
'''
3/2 x + 7/3 y = 10
16/3 x + 37/21 =  149/21
'''
def skracanie(l, m):
    if(l==0):
        return (0, 1)
    if(l*m<0):
        l, m = abs(l), abs(m)
        z=-1
    else:
        z=1
    D=[[1], [1]]
    for i in range(1, l//2+1):
        if(l%i==0):
            D[0].append(i)
    for i in range(1, m//2+1):
        if(m%i==0):
            D[1].append(i)
    for k in D[0][::-1]:
        if k in D[1]:
            l//=k
            m//=k
            if(z==-1):
                l*=-1
            return (l, m)

def skr(l, m):
    def nwd(l, m):
        while(m!=0):
            l, m = l, l%m
        return l
    return l//nwd(l, m), m//nwd(l, m)

def roznica(a, b):
    m=a[1]*b[1]
    l=a[0]*b[1]-b[0]*a[1]
    w=skracanie(l, m)
    return w

def iloraz(a, b):
    l=a[0]*b[1]
    m=a[1]*b[0]
    w=skracanie(l, m)
    return w

T1=[(3, 2), (7, 3), (10, 1)]
T2=[(16, 3), (37, 21), (149, 21)]

k=iloraz(T1[0], T2[0])
for i in range(3):
    T2[i]=(k*T2[i][0], k*T2[i][1])
    
for i in range(3):
    T2[i]=roznica(T2[i], T1[i])
print(T1[:])
print(T2[:])
#cos nie dziala
