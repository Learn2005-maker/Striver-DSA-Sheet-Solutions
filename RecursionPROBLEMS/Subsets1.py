# Time Complexity: O(2^n)
# Space Complexity: O(n) for the recursion stack

def Subsets(index,curds,cursum,nums,ans):
    if index==len(nums):
        ans.append(cursum)
        return
    curds.append(nums[index])
    cursum+=nums[index]
    Subsets(index+1,curds,cursum,nums,ans)
    curds.pop()
    cursum-=nums[index]
    Subsets(index+1,curds,cursum,nums,ans)


nums=[2,3]
ans=[]
Subsets(0,[],0,nums,ans)
print(ans)