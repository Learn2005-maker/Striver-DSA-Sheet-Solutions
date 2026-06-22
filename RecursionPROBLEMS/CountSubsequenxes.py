# Time complexcity:O(N*2^N)
# space complexity:O(N) - to store the powerset

powerSet=[]
count=0
def Countsubseqs(nums,st_index,curr_subset):
    global count
    if st_index>=len(nums):
        powerSet.append(curr_subset[:])
        count+=1
        return
    curr_subset.append(nums[st_index])
    Countsubseqs(nums,st_index+1,curr_subset)
    curr_subset.pop()    
    Countsubseqs(nums,st_index+1,curr_subset)
nums = [4, 9, 2, 5, 1]
# k = 10        

Countsubseqs(nums,0,[]) 
print(count)
print(powerSet)