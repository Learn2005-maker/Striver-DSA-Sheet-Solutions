nums=[5,7,9,10,3,4]
n=len(nums)
stack=[]
nge=[-1]*n
for  i in range(n):
    while stack and stack[-1]>=nums[i]:
        stack.pop()
    if stack:
        nge[i]=stack[-1]
    stack.append(nums[i])
print(nge) 



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