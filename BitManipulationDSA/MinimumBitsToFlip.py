start=10
goal=7
ans=start^goal
count=0
for i in range(0,32):
    if ans & (1<<i):
        count+=1
print(count)       

# Time Complexcity : O(31)


# Time complexcity: O(1) 
n=start^goal
count=0
while n!=0:
    n=n&n-1
    count+=1
print(count)   