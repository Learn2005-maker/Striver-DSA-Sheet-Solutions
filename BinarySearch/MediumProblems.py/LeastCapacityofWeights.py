# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.


def leastCapacity(weights,cap):
    day=1
    load=0
    for num in weights:
        if load+num>cap:
            day=day+1
            load=num
        else:
            load+=num
    return day        
            
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

for i in range(max(weights),sum(weights)):
    daysRequired=leastCapacity(weights,i)
    if daysRequired<=days:
        print(i)
        break

    # Time complexcity:O(nlogn)
def leastCapacity(weights,cap):
    day=1
    load=0
    for num in weights:
        if load+num>cap:
            day=day+1
            load=num
        else:
            load+=num
    return day        
            
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

low=max(weights)
high=sum(weights)

while low<=high:
    mid=(low+high)//2
    if leastCapacity(weights,mid)<=days:
        high=mid-1
    else:
        low=mid+1
print(low)        
    