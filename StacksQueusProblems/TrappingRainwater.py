def trap(height):
    n=len(height)
    total=0
    prefix_max=[0]*n
    suffix_max=[0]*n
    prefix_max[0]=height[0]
    for i in range(1,n):
        
        prefix_max[i]=max(prefix_max[i-1],height[i])
    suffix_max[n-1]=height[n-1]
    for i in range(n-2,-1,-1):
        suffix_max[i]=max(suffix_max[i+1],height[i])
    
    for i in range(n):
        left_max=prefix_max[i]
        right_max=suffix_max[i]
        if height[i]<left_max and height[i]<right_max:
            total=total+min(left_max,right_max)-height[i]
    return total

height=[0,1,0,2,1,0,1,3,2,1,2,1]

res=trap(height)
print(res)
# Time complexcity:O(3n)
# Space complexcity:O(2n)



# You can also do with O(n) space and O(n) time complexcity by using only suffix_max array and left_max variable.
def trap(height):
    n=len(height)
    total=0
    # prefix_max=[0]*n
    suffix_max=[0]*n
    # prefix_max[0]=height[0]
    # for i in range(1,n):
        
    #     prefix_max[i]=max(prefix_max[i-1],height[i])
    suffix_max[n-1]=height[n-1]
    for i in range(n-2,-1,-1):
        suffix_max[i]=max(suffix_max[i+1],height[i])
    left_max=0
    for i in range(n):
        left_max=max(left_max,height[i])
        right_max=suffix_max[i]
        if height[i]<left_max and height[i]<right_max:
            total=total+min(left_max,right_max)-height[i]
    return total

height=[0,1,0,2,1,0,1,3,2,1,2,1]

res=trap(height)
print(res)
