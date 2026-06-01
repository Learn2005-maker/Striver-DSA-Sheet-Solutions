# Brute Force Approach: O(n1 + n2) time complexity, O(n1 + n2) space complexity :O(n1 + n2) where n1 and n2 are the lengths of the two input arrays
arr1 = [2, 4, 6]
arr2 = [1, 3, 5]

n1 = len(arr1)
n2 = len(arr2)

i = 0
j = 0
nums = []

while i < n1 and j < n2:
    if arr1[i] <= arr2[j]:
        nums.append(arr1[i])
        i += 1
    else:
        nums.append(arr2[j])
        j += 1

while i < n1:
    nums.append(arr1[i])
    i += 1

while j < n2:
    nums.append(arr2[j])
    j += 1

n3 = len(nums)

# Median logic
if n3 % 2 != 0:
    print(float(nums[n3 // 2]))   # ✅ integer division
else:
    print((nums[n3 // 2] + nums[n3 // 2 - 1]) / 2)  # ✅ correct formula
    
    # Without using extra space: O(n1 + n2) time complexity, O(1) space complexity This code will works.....  
arr1 = [2, 4, 6]
arr2 = [1, 3, 5]

n1 = len(arr1)
n2 = len(arr2)

n = n1 + n2

# middle indices
ind1 = (n // 2) - 1
ind2 = (n // 2)

i = j = 0
cnt = 0

ind1el = -1
ind2el = -1

# merge without storing
while i < n1 and j < n2:
    if arr1[i] < arr2[j]:
        if cnt == ind1:
            ind1el = arr1[i]
        if cnt == ind2:
            ind2el = arr1[i]
        cnt += 1
        i += 1
    else:
        if cnt == ind1:
            ind1el = arr2[j]
        if cnt == ind2:
            ind2el = arr2[j]
        cnt += 1
        j += 1

# remaining elements
while i < n1:
    if cnt == ind1:
        ind1el = arr1[i]
    if cnt == ind2:
        ind2el = arr1[i]
    cnt += 1
    i += 1

while j < n2:
    if cnt == ind1:
        ind1el = arr2[j]
    if cnt == ind2:
        ind2el = arr2[j]
    cnt += 1
    j += 1
# median
if n % 2 == 1:
    print(ind2el)
else:
    print((ind1el + ind2el) / 2)   
    
    
        
# Time complexity: O(log(min(n1, n2))) using Binary Search
# One of the hardest problems in Binary Search is to find the median of two sorted arrays.
# The optimal solution for this problem has a time complexity of O(log(min(n1, n2))) where n1 and n2 are the lengths of the two input arrays.
def median(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)

    # हमेशा binary search छोटी array पर लगाना है
    # इसलिए अगर nums1 बड़ी है तो swap कर देते हैं
    # We are swapping the arrays to ensure that we always perform binary search on the smaller array, 
    # which optimizes the time complexity to O(log(min(n1, n2))). This is crucial because the binary search will be more efficient on the
    # smaller array, reducing the number of iterations needed to find the correct partition.
    if n1 > n2:
        return median(nums2, nums1)

    # binary search range
    low = 0
    high = n1

    # total elements in left partition
    left = (n1 + n2 + 1) // 2

    # total length
    n = n1 + n2

    while low <= high:
        # partition of nums1
        mid1 = (low + high) // 2

        # partition of nums2 (based on left size)
        mid2 = left - mid1

        # initialize with extreme values (for edge cases)
        l1 = float("-inf")   # left side max of nums1
        l2 = float("-inf")   # left side max of nums2
        r1 = float("inf")    # right side min of nums1
        r2 = float("inf")    # right side min of nums2

        # check bounds before accessing
        if mid1 < n1:
            r1 = nums1[mid1]
        if mid2 < n2:
            r2 = nums2[mid2]

        if mid1 - 1 >= 0:
            l1 = nums1[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = nums2[mid2 - 1]

        # correct partition condition
        if l1 <= r2 and l2 <= r1:

            # if total elements are odd
            if n % 2 == 1:
                return max(l1, l2)

            # if even, take average of middle two
            return (max(l1, l2) + min(r1, r2)) / 2.0

        # move left in nums1
        elif l1 > r2:
            high = mid1 - 1

        # move right in nums1
        else:
            low = mid1 + 1

    # fallback (should not reach here)
    return 0        