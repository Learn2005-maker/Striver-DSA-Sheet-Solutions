# Time complexcity:O(N*2^N)
# space complexity:O(N) - to store the powerset

# This is main answer to count the number of subsequences whose sum is equal to k
count=0
def Countsubseqs(nums,st_index,curr_subset,k):
    global count
    if st_index>=len(nums):
        if sum(curr_subset[:])==k:
            count+=1    
        return
    curr_subset.append(nums[st_index])
    Countsubseqs(nums,st_index+1,curr_subset,k)
    curr_subset.pop()    
    Countsubseqs(nums,st_index+1,curr_subset,k)
nums = [4, 2,10,5,1,3]
k = 5  

Countsubseqs(nums,0,[],k) 
print(count)






# This is to count the number of subsequences in an array
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



# This is to check if there is a subsequence whose sum is equal to k true or false
def Countsubseqs(nums,st_index,curr_sum,k):
    # global count
    if st_index>=len(nums):  
        return curr_sum==k
    if Countsubseqs(nums,st_index+1,curr_sum+nums[st_index],k):
        return True
    if Countsubseqs(nums,st_index+1,curr_sum,k):
        return True
    return False
nums = [1, 2, 3, 4, 5]
k = 8

print(Countsubseqs(nums,0,0,k) )