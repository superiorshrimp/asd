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

class Stack:
    def __init__(self):
        self.top=None
        self.count=0
    def stack_size(self):
        return self.count
    def empty(self):
        if self.count==0:
            return True
        else:
            return False
    def get(self):
        if self.stack_size()!=0:
            element=self.top
            self.top=element.next
            self.count-=1
            return element.val
    def put(self, element):
        new=Node(element)
        if self.stack_size()!=0:
            element=self.top
            new.next=element
            self.top=new
            self.count+=1
        else:
            self.count=1
            self.top=new

#przykład:

def make_q(T):
    q=Queue()
    for el in T:
        q.put(el)

def make_stack(T):
    stack=Stack()
    for el in T:
        stack.put(el)
