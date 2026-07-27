from collections import deque
class MyStack:
    def __init__(self):
        self.q=deque()
    def push(self,x):
        self.q.append(x)
        for i in range(len(self.q)-1):
            value=self.q.popleft()
            self.q.append(value)
    def pop(self):
        return self.q.popleft()
    def top(self):
        return self.q[0]
    def empty(self):
        return len(self.q)==0
    def display(self):
        print("Stack:",list(self.q))

s=MyStack()
s.push(9)
s.push(10)
s.push(11)

s.display()
print("top element",s.top())
# s.display()

print("poped element:",s.pop())
s.display()