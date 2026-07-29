# stack=[]
# stack.append([9,9])
# stack.append([10,5])
# print(stack[-1][1])

class MinStack():
    def __init__(self):
        self.stack=[]
    def push(self,value):
        if len(self.stack)==0:
            self.stack.append([value,value])
        else:
            self.stack.append([value,min(value,self.stack[-1][1])])
    def pop(self):
        return self.stack.pop()[0]
    def top(self):
        return self.stack[-1][0]
    def getMin(self):
        return self.stack[-1][1]
        
obj=MinStack()
obj.push(10)
obj.push(30)
obj.push(40)
print("pop element",obj.pop())
print("top element",obj.top())
print("Minimum element:", obj.getMin())
        