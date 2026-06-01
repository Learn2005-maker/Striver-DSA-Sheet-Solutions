# BRUTE FORCE
# Time Complexity: O(m + n)
# Space Complexity: O(1)

def kthElement(nums1, nums2, k):
    nums1.sort()
    nums2.sort()
    
    i = j = 0
    count = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            count += 1
            if count == k:
                return nums1[i]
            i += 1
        else:
            count += 1
            if count == k:
                return nums2[j]
            j += 1

    # remaining elements
    while i < len(nums1):
        count += 1
        if count == k:
            return nums1[i]
        i += 1

    while j < len(nums2):
        count += 1
        if count == k:
            return nums2[j]
        j += 1
k=5
print(kthElement([2, 3, 6, 7, 9], [1, 4, 8, 10], k))   


 # Optimized Approach using Binary Search
# Time Complexity: O(log(min(n1, n2)))

def kthElement(nums1,nums2,k):
    n1=len(nums1)
    n2=len(nums2)
    if n1>n2:
        return kthElement(nums2,nums1,k)
    low=max(0,k-n2)
    high=min(k,n1)
    while low<=high:
        mid1=(low+high)//2
        mid2=k-mid1
        l1=float("-inf")
        l2=float("-inf")
        r1=float("inf")
        r2=float("inf")
        if mid1<n1:
            r1=nums1[mid1]
        if mid2<n2:
            r2=nums2[mid2]
        if mid1>0:
            l1=nums1[mid1-1]
        if mid2>0:
            l2=nums2[mid2-1]
        if l1<=r2 and l2<=r1:
            return max(l1,l2)
        elif l1>r2:
            high=mid1-1
        else:
            low=mid1+1
nums1=[4,9,6,10]
nums2=[1,2,8]

k=7
print(kthElement(nums1,nums2,k))  