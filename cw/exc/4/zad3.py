from math import inf

class bst_node:
    def __init__(self,key,sumleft=0,sumright=0,left=None,right=None):
        self.key = key
        self.sumleft = sumleft
        self.sumright = sumright
        self.left = left
        self.right = right
    def __str__(self):
        ret = ""
        if self.left:
            ret += str(self.left) + "<"
        ret += str(self.key)
        if self.right:
            ret += "<" + str(self.right)
        return ret

def insert(root,key) -> bst_node:
    if root is None:
        return bst_node(key)
    if key<root.key:
        root.sumleft+=key
        if root.left is None:
            new=bst_node(key)
            root.left=new
            return
        insert(root.left, key)
    else:
        root.sumright+=key
        if root.right is None:
            new=bst_node(key)
            root.right=new
            return 
        insert(root.right, key)

def left(root, val):
    if root is None:
        return 0
    if root.key<val:
        return left(root.right, val)-root.key-root.sumleft
    else:
        return left(root.left, val)

def right(root, val):
    if root is None:
        return 0
    if root.key>val:
        return right(root.left, val)-root.key-root.sumright
    else:
        return right(root.right, val)

def suma(root,x,y) -> float:
    if x==y:
        return 0
    common=root
    while True:
        if common is None:
            return 0
        if x<common.key and y<common.key:
            common=common.left
        elif x>common.key and y>common.key:
            common=common.right
        else:
            break
    if common.key==x:
        suma=common.key+common.sumright+right(common.right, y)
    elif common.key==y:
        suma=common.key+common.sumleft+left(common.left, x)
    else:
        suma=common.key+common.sumleft+common.sumright+left(common.left, x)+right(common.right, y)
    return suma


# testy:
T = [-1.0,-2.0,-1.1,10.0,9.0,9.5,0.5,10.5,10.2,5.0]
root = None
for elem in T:
    if root is None:
        root = insert(root,elem)
    else:
        insert(root,elem)
print(suma(root,-2.0,-1.0),"?=?",-4.1)
insert(root,-1.5)
print(suma(root,-2.0,-1.0),"?=?",-5.6)

print(suma(root,5.0,9.5),"?=?",5.0 + 9.0 + 9.5)
insert(root,6.7)
print(suma(root,5.0,9.5),"?=?",5.0 + 9.0 + 9.5 + 6.7)
print(suma(root,-inf,inf),"?=?",55.8)
#close enough
#co prawda moze nie jest logn bo nie jest zrownowazone ale 1 punkt by był