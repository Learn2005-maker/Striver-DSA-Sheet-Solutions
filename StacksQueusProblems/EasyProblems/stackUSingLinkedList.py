class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
        
    def push(self,value):
        newnode=Node(value)
        newnode.next=self.top
        self.top=newnode
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return None
        value=self.top.data
        self.top=self.top.next
        return  value 
    def peek(self):
        if self.top is None:
            print("Stack Underflow")
            return None
        
        return self.top.data
    def isEmpty(self):
        return self.top is None
    def display(self):
        if self.top is None:
            print("Stack is Empty")
            return
        temp=self.top
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()    
s=Stack()

s.push(10)
s.push(90)
s.push(20)
s.push(30)

s.display()
print("Top:", s.peek())
print("Pop:", s.pop())
s.display()
