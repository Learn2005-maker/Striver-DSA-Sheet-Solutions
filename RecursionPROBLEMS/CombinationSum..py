# Time complexxity:O(2^n*k) where k is avg length of output combinations
# s.c:O(n) recursion stack
def combinationSum2(index,target,arrds,candidates,ans):
    if target==0:
        ans.append(arrds[:])
        return    
    for i in range(index,len(candidates)):
        if  i>index and candidates[i]==candidates[i-1]:
            continue
        if candidates[i]>target:
            break
        arrds.append(candidates[i])
        combinationSum2(i+1,target-candidates[i],arrds,candidates,ans)
        arrds.pop()
candidates = [1,1,1,2,2]
candidates.sort()
target = 4
ans=[]
combinationSum2(0,target,[],candidates,ans)
print(ans)
