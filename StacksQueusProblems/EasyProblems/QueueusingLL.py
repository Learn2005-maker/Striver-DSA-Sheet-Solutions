class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        
    def enqueue(self,value):
        newnode=Node(value)
        if self.rear is None:
            self.front=self.rear=newnode
            return
        self.rear.next=newnode
        self.rear=newnode

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return None
        value=self.front.data
        self.front=self.front.next
        return  value 
        
    def peek(self):
        if self.front is None:
            print("Queue is Empty")
            return None
        
        return self.front.data
        
    def isEmpty(self):
        return self.front is None
        
    def display(self):
        if self.front is None:
            print("Queue is Empty")
            return
        temp=self.front
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()    
        
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Front:", q.peek())
print("Dequeue:", q.dequeue())

q.display()

# Maintain two pointers:

# front → First node
# rear → Last node
# Enqueue: Insert at the rear.
# Dequeue: Remove from the front.
