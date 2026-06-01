nums1 = [1, 2, 3, 4, 5]

nums2 = [1, 2, 7]


a=set(nums1)|set(nums2)

print(list(a))


# Manual method (no sets — for understanding logic)
# ➡️ Slower for big lists, but good for beginners to understand how union logic works.
nums1 = [1, 2, 3, 4, 5]

nums2 = [1, 2, 7]
arr=[]
for i in nums1+nums2:
    if i not in arr:
        arr.append(i)
        
        
print(arr)        
    