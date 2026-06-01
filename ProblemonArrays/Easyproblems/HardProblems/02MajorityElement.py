# Brute force Solution
# Time Complexity: O(N) where N is the number of elements in the array
# Space Complexity: O(N)
def majorityElement(nums):
        n=len(nums)
        ans=[]
        dici={}       
        for num in nums:
            dici[num]=dici.get(num,0)+1
        # print(dici)
        for key,j in dici.items():
            if j>n//3:
                ans.append(key)
        return ans    
    
    
nums = [1, 2]
n=len(nums)

# We are checking Majority ||  > n/3..

nums=[1,2,3,4]
cand1=0
cand2=0
count1=0
count2=0

for num in nums:
    if cand1==num:
        count1+=1
    elif cand2==num:
        count2+=1
    elif count1==0:
        cand1=num
        count1=1
    elif count2==0:
        cand2=num 
        count2=1
    else:
        count1-=1
        count2-=1
# verifying
ans=[]
if nums.count(cand1)>n//3:
    ans.append(cand1)
if cand1!=cand2 and nums.count(cand2)>n//3:
    ans.append(cand2)    

print(ans)            