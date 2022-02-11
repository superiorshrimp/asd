'''
Zadanie 10. Rekurencyjne obliczanie wyznacznika z macierzy (treść oczywista)
'''

def f(M, s, i):
    if(i==2*len(M)):
        return s
    if(i<len(M)):
        w=1
        for k in range(len(M)):
            w*=M[k][(i+k)%len(M)]
        print(w, s+w)
        return f(M, s+w, i+1)
    else:
        w=1
        for k in range(len(M)):
            w*=M[k][(i+k)%len(M)]
        print(w, s-w)
        return f(M, s-w, i+1)
            
M=[1, 2, 3], [1, 1, 1], [3, 2, 1]


print(f(M, 0, 0))