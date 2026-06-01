from math import ceil

def noofBananasEating(piles, k):    
    totalhrs = 0
    for pile in piles:
        totalhrs += ceil(pile / k)
    return totalhrs    

piles = [3,6,7,11]
h = 8

for k in range(1, max(piles) + 1):
    reqTime = noofBananasEating(piles, k)
    if reqTime <= h:
        print(k)
        break

# Time: O(max(piles) * n)    # 
# It has time limit Exceeded
    

# Using binary search for finding minimum eating speed
from math import ceil
def noofBananasEating(piles, k):    
    totalhrs = 0
    for pile in piles:
        totalhrs += ceil(pile / k)
    return totalhrs  
piles=[3,6,7,11]
h=8
low=1
high=max(piles)

while low<=high:
    mid=(low+high)//2
    reqTime=noofBananasEating(piles,mid)
    if reqTime<=h:
        ans=mid
        high=mid-1
    else:
        low=mid+1
        
print(ans)