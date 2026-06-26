# this problme is similar to the previous problem but here we have to find the unique subsets of the given array. 
# The array may contain duplicates. So we will sort the array first and then we will check if the current element is same as the previous element 
# then we will skip that element.
# Time Complexity: O(2^n*n) because we are generating all the subsets and for each subset we are copying the current subset to the answer list.
# Space Complexity: O(n) for the recursion stack
def Subsets(index,curds,nums,ans):
    if index==len(nums):
        ans.append(curds[:])
        return
    for i in range(index,len(nums)):
        if i>index and nums[i]==nums[i-1]:
            continue
        Subsets(i+1,curds+[nums[i]],nums,ans)
    
    Subsets(i+1,curds,nums,ans)


nums=[4,4,4,1,4]
nums.sort()
ans=[]
Subsets(0,[],nums,ans)
print(ans)
