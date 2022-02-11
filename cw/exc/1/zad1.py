#Szymon Żychowicz
'''
algorytm zachłanny:
dla każdej litery alfabetu łacińskiego powstaje początkowo pusta kolejka
dla każdej litery wyrazu x jej indeks w wyrazie jest dodawany do kolejki odpowiedniej litery
powoduje to to, że mogę potem je ściągać w rosnącej kolejności
potem dla każdej litery wyrazu y jeśli kolejka liery jest pusta to znaczy, że jest inna liczba tych liter w wyrazach - zwraca False
jeśli nie to sprawdza czy różnica ich indeksów jest większa od t - jeśli tak to zwraca False
dowód:
jeśli nie połączy się wsytąpień konkretnej litery w wyrazach pierwsza z pierwszą, druga z druga itd to rozwiązanie może nie istnieć,
bo każda litera musi zostać wykorzystana, a im później wybierze się daną tym większa szansa, że beżie dalej niż pozwala t
złożoność: O(n+k)
'''

from zad1testy import runtests
from queue import Queue

class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next

class Queue:
    def __init__(self):
        self.first=None
        self.last=None
        self.count=0
    def q_size(self):
        return self.count
    def empty(self):
        if self.count==0:
            return True
        else:
            return False
    def get(self):
        if self.q_size()!=0:
            element=self.first
            self.first=element.next
            self.count-=1
            return element.val
    def put(self, new_value):
        new=Node(new_value)
        if self.q_size()!=0:
            element=self.last
            element.next=new
            self.last=new
            self.count+=1
        else:
            self.count=1
            self.first=new
            self.last=new

def tanagram(x, y, t):
    T=[Queue() for _ in range(ord("z")-ord("a"))]
    for i in range(len(x)):
        T[ord(x[i])-ord("a")-1].put(i)
    for i in range(len(y)):
        if T[ord(y[i])-ord("a")-1].empty() is True:
            return False
        else:
            q=T[ord(y[i])-ord("a")-1].get()
            if abs(i-q)>t:
                return False
    return True

runtests(tanagram)