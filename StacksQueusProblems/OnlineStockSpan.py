# Brute Force:O(no.ofdays) and S.c:O(total next cells)
class StockSpanner:
    def __init__(self):
        self.arr=[]
    def next(self,value):
        self.arr.append(value)
        count=1
        for i in range(len(self.arr)-2,-1,-1):
            if self.arr[i]<=value:
                count+=1
            else:
                break
        return count            

s = StockSpanner()
prices_to_process = [100, 80, 60, 70, 60, 75]
output = []

for price in prices_to_process:
    span=s.next(price)
    output.append(span)
print(output)    



# Time complxity:O(n)
class StockSpanner:
    def __init__(self):
        self.stack=[]
        self.idx=-1
    def next(self,value):
        self.idx+=1
        while self.stack and self.stack[-1][0]<=value:
            self.stack.pop()
        ans=self.idx-(self.stack[-1][1] if self.stack else -1)
        self.stack.append([value,self.idx])     
        return ans           

s = StockSpanner()
prices_to_process = [100, 80, 60, 70, 60, 75]
output = []

for price in prices_to_process:
    span=s.next(price)
    output.append(span)
print(output)    