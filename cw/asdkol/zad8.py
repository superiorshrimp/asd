from zad2testy import runtests
from math import inf

class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

def rek(root):
    if root.right is None and root.left is None: #jeśli liść
        return inf
    if root.left is None:
        return root.value
    elif root.right is None:
        return min(root.value, rek(root.left))
    else:
        return min(root.value, rek(root.left)+rek(root.right)) 
        
def cutthetree(T):
    return rek(T.left)+rek(T.right) #z polecenia wiemy że nie trzeba sprawdzać tu żadnych None

runtests(cutthetree)