# Brute Force:O(no.ofdays) and s.c:O(total next cells)
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