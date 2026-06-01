# You are given an integer array bloomDay, an integer m and an integer k.

# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
# Example 1:

# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
# Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, _, _, _, _]   // we can only make one bouquet.
# After day 2: [x, _, _, _, x]   // we can only make two bouquets.
# After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.


def ispossible(bloomDay,m,k,day):
    n=len(bloomDay)
    count=0
    noofBouques=0
    for num in bloomDay:
        if num<=day:
            count+=1
        else:
            noofBouques+=count//k
            count=0
    noofBouques+=count//k
    if noofBouques>=m:
        return True
    else:
        return False


bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3

ans=-1
for i in range(min(bloomDay),max(bloomDay)+1):
    if ispossible(bloomDay,m,k,i)==True:
        ans=i
        break
print(ans)        
    
    
    # Using Binary Search Answer
    # Time complexcity:O(nlogn)
def ispossible(bloomDay,m,k,day):
    n=len(bloomDay)
    count=0
    noofBouques=0
    for num in bloomDay:
        if num<=day:
            count+=1
        else:
            noofBouques+=count//k
            count=0
    noofBouques+=count//k
    if noofBouques>=m:
        return True
    else:
        return False
        
bloomDay = [1,10,3,10,2]
m = 3
k = 1

ans=-1
low=min(bloomDay)
high=max(bloomDay)
while low <= high:
    mid=(low+high)//2
    if ispossible(bloomDay,m,k,mid)==True:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)    