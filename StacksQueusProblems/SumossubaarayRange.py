# Brute force 
# Sum of Subarray range 
# Time complxity:O(n) and S.c : O(n)
arr=[1,2,3]
n=len(arr)

sum=0
for i in range(n):
    largest=arr[i]
    smallest=arr[i]
    for j in range(i,n):
        largest=max(largest,arr[j])
        smallest=min(smallest,arr[j])
        sum=sum+(largest-smallest)

print(sum)        

def subArrayRanges(nums):
    # Sumof subArray minimums
    n=len(nums)
    nge=[n]*n
    psee=[-1]*n
    stack=[]
    for i in range(n):
        while stack and nums[stack[-1]]>nums[i]:
            stack.pop()
        if stack:
            psee[i]=stack[-1]
        stack.append(i) 
    
    stack=[]
    for i in range(n-1,-1,-1):
        while stack and nums[stack[-1]]>=nums[i]:
            stack.pop()
        if stack:
            nse[i]=stack[-1]
        stack.append(i)
    min_sum=0
    for i in range(n):
        left=i-psee[i]
        right=nse[i]-i
        min_sum=min_sum+(left*right*nums[i])

    # Sum of Subarray maximums.
    pge=[-1]*n
    nge=[n]*n
    for i in range(n):
        while stack and nums[stack[-1]]<nums[i]:
            stack.pop()
        if stack:
            pge[i]=stcak[-1]
        stack.append(i)    
    
    for i in range(n-1,-1,-1):
        while stack and nums[stack[-1]]<=nums[i]:
            stack.pop()
        if stack :
            nge[i]=stcak[-1]
        stack.append(i)  
    maxi_sum=0   
    for i in range(n):
        left=i-pge[i]
        right=nge[i]-i
        maxi_sum=maxi_sum+(left*right*nums[i])

    return maxi_sum-min_sum
    

    
nums=[1,2,3]

print(subArrayRanges(nums))




