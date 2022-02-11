#Szymon Żychowicz

def rek(T, row, col, i, w, k, max1, max2):
    w[row]+k[kol]

def chess(T):
    w=[]    #wyliczam sumy wierszy
    for i in range(len(T)):
        suma=0
        for j in range(len(T)):
            suma+=T[i][j]
        w.append(suma)
    k=[]    #wyliczam sumy kolumn
    for j in range(len(T)):
        suma=0
        for i in range(len(T)):
            suma+=T[i][j]
        k.append(suma)
    max1=0
    max2=0
    max1coord=(-1,-1)
    max2coord=(-1,-1)
    for row in range(len(w)):
        for col in range(len(k)):
            if(w[row]+k[col]-T[row][col]>max1): #wyliczam czy suma wiersza + kolumny - pola jest najwieksza
                max1=w[row]+k[col]-T[row][col]
                max1coord=(row, col)
            elif(w[row]+k[col]-T[row][col]>max2): #jesli nie to czy jest druga najwieksza
                max2=w[row]+k[col]-T[row][col]
                max2coord=(row, col)
    maxcoord=(max1coord[0],max1coord[1],max2coord[0],max2coord[1],)
    return maxcoord
#zapomnialem ze 2 pola sa szachowane ale zorientowalem sie na koniec czasu