class Queue:
    def __init__(self,size):
        self.queue=[0]*size
        self.front=0
        self.rear=-1
        self.size=size
    def enqueue(self,value):
        if self.rear==self.size-1:
            print("Queue Overflow")
            return 
        self.rear+=1
        self.queue[self.rear]=value
    def dequeue(self):
        if self.front>self.rear:
            print("Queue Underflow")
            return None
        value=self.queue[self.front]    
        self.front+=1
        return value
    def  peek(self):
        if self.front>self.rear:
            print("Queue is Empty")
            return None
        return self.queue[self.front]
    def isEmpty(self):
        return self.front>self.rear
        
    def display(self):
        if self.front>self.rear:
            print("Queue is Empty")
            return
        for i in range(self.front,self.rear+1):
            print(self.queue[i],end=" ")
        print()    
q = Queue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(10)
q.enqueue(20)
# q.enqueue(30)
q.display()

print("Front:", q.peek())
print("Dequeue:", q.dequeue())

q.display()

print(q.isEmpty())
        
