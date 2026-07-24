class Stack:
    def __init__(self,size):
        self.stack=[0]*size
        self.top=-1
        self.size=size
    def push(self,value):
        if self.top==self.size-1:
            print("Stack Overflow")
            return 
        self.top+=1
        self.stack[self.top]=value
    def pop(self):
        if self.top==-1:
            print("Stack Underflow")
            return None
        value=self.stack[self.top]    
        self.top-=1
        return value
    def  peek(self):
        if self.top==-1:
            print("Stack is Empty")
            return None
        return self.stack[self.top]
    def isEmpty(self):
        return self.top==-1 
        
    def display(self):
        if self.top==-1:
            print("Stack is Empty")
            return
        for i in range(self.top,-1,-1):
            print(self.stack[i],end=" ")
        print()    
        
s=Stack(5)  # Define the Size first.
s.push(10)
s.push(30)
s.push(20)
s.display()

print("Top Element:",s.peek())
print()
print("Popped Element:",s.pop())
print()
print(s.isEmpty())

s.display()
# Time complexcity:O(1)
# Sapce complexcity:O(size of stack)

        
