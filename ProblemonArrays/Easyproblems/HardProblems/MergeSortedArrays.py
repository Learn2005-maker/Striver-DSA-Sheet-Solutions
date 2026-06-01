
# iven two integer arrays nums1 and nums2. Both arrays are sorted in non-decreasing order.
# Merge both the arrays into a single array sorted in non-decreasing order.
# The final sorted array should be stored inside the array nums1 and it should be done in-place.
# nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s.
# nums2 has a length of n.

# Example 1

# Input: nums1 = [-5, -2, 4, 5], nums2 = [-3, 1, 8]

# Output: [-5, -3, -2, 1, 4, 5, 8]

# Explanation:

# The merged array is: [-5, -3, -2, 1, 4, 5, 8], where [-5, -2, 4, 5] are from nums1 and [-3, 1, 8] are from nums2
nums1 = [-5, -2, 4, 5]
nums2 = [-3, 1, 8]

n=len(nums1)
m=len(nums2)

i=0
j=0
result=[]
while i < n and j< m:
    if nums1[i]<=nums2[j]:
        result.append(nums1[i])
        i+=1
    else:
        result.append(nums2[j])
        j+=1
# Add remaining elements    
while i<n:
    result.append(nums1[i])
    i+=1
while j<m:
    result.append(nums2[j])
    j+=1
print(result)
for i in range(n+m):
    if i<n:
        nums1[i]=result[i]
    else:
        nums2[i-n]=result[i]
print(nums1+nums2)        

#Time complexity: O(n+m)
#  Space complexity: O(n+m) due to the result array. We can optimize it to O(1) by modifying nums1 in-place from the end. 
    
    
#  Optimal  Approach: O(min(n,m))+O(nlogn)+ O(mlogm) time and O(1) space
nums1 = [-5, -2, 4, 5]
nums2 = [-3, 1, 8]

m=4
n=3
i=m-1
j=0

while i>=0 and j<m:
    if nums1[i]>nums2[j]:
        nums1[i],nums2[j]=nums2[j],nums1[i]# Swap
        i-=1
        j+=1
    else:
        break
nums1[:m]=sorted(nums1)  
nums2[:]=sorted(nums2)
nums1[m:]=nums2      
print(nums1)   


nums1 = [-5, -2, 4, 5,0,0,0]
nums2 = [-3, 1, 8]

n=4
m=3
gap = (n + m + 1) // 2

while gap > 0:
    i = 0
    j = gap
    
    while j < (n + m):
        
        # Case 1: both in nums1
        if i < n and j < n:
            if nums1[i] > nums1[j]:
                nums1[i], nums1[j] = nums1[j], nums1[i]
        
        # Case 2: i in nums1, j in nums2
        elif i < n and j >= n:
            if nums1[i] > nums2[j - n]:
                nums1[i], nums2[j - n] = nums2[j - n], nums1[i]
        
        # Case 3: both in nums2
        else:
            if nums2[i - n] > nums2[j - n]:
                nums2[i - n], nums2[j - n] = nums2[j - n], nums2[i - n]
        
        i += 1
        j += 1
    
    if gap == 1:
        gap = 0
    else:
        gap = (gap + 1) // 2
for i in range(m):
    nums1[n+i]=nums2[i]
print(nums1)



# Optimal Appraoch: O(n+m) time and O(1) space

nums1 = [-5, -2, 4, 5,0,0,0] # --> THIS is leetcode format style. 
nums2 = [-3, 1, 8]
m=4
n=3

i=m-1
j=n-1
k=m+n-1 # Last index of K

while j>=0:
    if i>=0 and nums1[i]>nums2[j]:
        nums1[k]=nums1[i]
        i-=1
    else:
        nums1[k]=nums2[j]    
        j-=1
    k-=1  
print(nums1)    
# Time complexcity: O(n+m)
# Space complexity: O(1) since we are modifying nums1 in-place. 
    



# Method	Time	Space	Interview Safe
# Swap + Sort	O(n log n)	O(1)	❌ Not optimal
# Gap Method	O((m+n) log(m+n))	O(1)	⚠️ Advanced
# 3 Pointer Back	O(m+n)	O(1)	✅ Best    
        