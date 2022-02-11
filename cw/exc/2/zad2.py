from zad2testy import runtests

def tower(A):
	maksimum=0
	F=[1 for _ in range(len(A))]
	for i in range(len(A)):
		for j in range(i):
			if A[j][0]<=A[i][0] and A[j][1]>=A[i][1]:
				F[i]=max(F[i], F[j]+1)
				maksimum=max(maksimum, F[i])
	print("aaa", F)
	return maksimum

runtests( tower )
