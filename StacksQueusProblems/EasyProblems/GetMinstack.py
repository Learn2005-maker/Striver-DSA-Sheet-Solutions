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

       
class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, value):
        if len(self.stack) == 0:
            self.mini = value
            self.stack.append(value)
        else:
            if value >= self.mini:
                self.stack.append(value)
            else:
                self.stack.append(2 * value - self.mini)
                self.mini = value

    def pop(self):
        if len(self.stack) == 0:
            return None

        x = self.stack.pop()

        if x >= self.mini:
            return x
        else:
            original = self.mini
            self.mini = 2 * self.mini - x
            return original

    def top(self):
        x = self.stack[-1]

        if x >= self.mini:
            return x
        else:
            return self.mini

    def getMin(self):
        return self.mini


obj = MinStack()

obj.push(10)
obj.push(30)
obj.push(5)
obj.push(2)

print("Minimum:", obj.getMin())
print("Top:", obj.top())
print("Pop:", obj.pop())
print("Minimum:", obj.getMin())
print("Top:", obj.top())       