# Time complexcity:O(N*2^N)
# space complexity:O(N*2^N) - to store the powerset
# iterative approach to generate powerset
nums=[1,2,3]

n=len(nums)
powerset=[[]]
for num in nums:
    subsets=[]
    for curr in powerset:
        subsets.append(curr+[num])
    powerset.extend(subsets)   
print(powerset)    
        

# Time complexcity:O(N*2^N)
# space complexity:O(N*2^N) - to store the powerset
nums=[1,2]
powerset=[]
def backtrack(s_index,cur_subset):
    if len(nums)==s_index:
        powerset.append(cur_subset[:])
        return
    cur_subset.append(nums[s_index])
    backtrack(s_index+1,cur_subset)
    cur_subset.pop()
    backtrack(s_index+1,cur_subset)

backtrack(0,[])
print(powerset)

# Take
# ↓
# Explore
# ↓
# Undo
# ↓
# Don't Take
# ↓
# Explore        
        


        