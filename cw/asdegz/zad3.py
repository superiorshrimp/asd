from zad3testy import runtests

def partition_x(T, l, p):
    pivot=T[p][0]
    j=l
    for i in range(l, p):
        if T[i][0]<=pivot:
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def quicksort_x(T, l, p):
    while l<p:
        q=partition_x(T, l, p)
        if abs(q-1-l)<abs(p-q+1):
            quicksort_x(T, l, q-1)
            l=q+1
        else:
            quicksort_x(T, q+1, p)
            p=q-1

def partition_y(T, l, p):
    pivot=T[p][1]
    j=l
    for i in range(l, p):
        if T[i][1]<=pivot:
            T[i], T[j] = T[j], T[i]
            j+=1
    T[p], T[j] = T[j], T[p]
    return j

def quicksort_y(T, l, p):
    while l<p:
        q=partition_y(T, l, p)
        if abs(q-1-l)<abs(p-q+1):
            quicksort_y(T, l, q-1)
            l=q+1
        else:
            quicksort_y(T, q+1, p)
            p=q-1

def overlapping(a, b):
    a1, a2, b1, b2 = a[0], a[1], b[0], b[1]
    if a1==b1:
        return None
    if b1<=a2 and b2>=a2:
        return True
    return False

def kintersect( T, k ):
	A=[T[i] for i in range(len(T))]
	quicksort_y(A, 0, len(A)-1)
	quicksort_x(A, 0, len(A)-1)
	F=[[0 for j in range(k+1)] for i in range(len(A))]
	Prev=[[(None, None) for j in range(k+1)] for i in range(len(A))]
	F[0][1]=A[0][1]-A[0][0]
	for i in range(1, len(A)):
		for j in range(i):
			if overlapping(A[j], A[i]) is None:
				for p in range(k+1):
					if F[i][p]<F[j][p]+A[i][1]-A[j][1]:
						F[i][p]=F[j][p]+A[i][1]-A[j][1]
						Prev[i][p]=Prev[j][p]
			if overlapping(A[j], A[i]) is True:
				for p in range(1,k+1):
					if F[i][p]<F[j][p-1]+A[i][1]-A[j][1]:
						F[i][p]=F[j][p-1]+A[i][1]-A[j][1]
						Prev[i][p]=(j, p-1)
		F[i][1]=max(F[i][1], A[i][1]-A[i][0])
	maksimum=0
	max_id=None
	for i in range(len(A)):
		if maksimum<F[i][k]:
			maksimum=F[i][k]
			max_id=(i, k)
	R=[]
	print(maksimum)
	if max_id is None:
		return []
	while max_id!=(None, None):
		R.append(max_id[0])
		max_id=(Prev[max_id[0]][max_id[1]][0], Prev[max_id[0]][max_id[1]][1])
	return R

#runtests( kintersect )
A = [(0,4),(1,10),(6,7), (2,8)]
k=3
print(kintersect(A, k))