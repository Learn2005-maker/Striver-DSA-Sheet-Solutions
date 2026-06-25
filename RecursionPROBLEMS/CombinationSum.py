# Time complexcity:O(N*2^N)
# space complexity:O(N) - to store the powerset

def combinationSum(index,target,arrds,candidates):
    if index==len(candidates):
        if target==0:
            print(arrds[:])
        return    
    if candidates[index]<=target:
        arrds.append(candidates[index])
        combinationSum(index,target-candidates[index],arrds,candidates)
        arrds.pop()
    combinationSum(index+1,target,arrds,candidates)
    



candidates = [2,3,6,7]
target = 7
combinationSum(0,target,[],candidates)