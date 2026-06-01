# Given an integer array nums. Return the number of inversions in the array.

# Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
# It indicates how close an array is to being sorted.
# A sorted array has an inversion count of 0.
# An array sorted in descending order has maximum inversion
# Brute Force Approach: O(n^2) time and O(1) space
nums=[5,3,2,4,1]
# count inversions
n=len(nums)
count=0
for i in range(n):
    for j in range(i+1,n):
        if nums[i]>nums[j] and i<j:
            count+=1
print(count)   

 # Optimal Approach: O(nlogn) time and O(n) space using merge sort  

def countInversions(arr):
    def merge_sort(arr, low, high):
        if low >= high:
            return 0
        
        mid = (low + high) // 2
        count = 0
        
        # Left half
        count += merge_sort(arr, low, mid)
        
        # Right half
        count += merge_sort(arr, mid + 1, high)
        
        # Merge step
        count += merge(arr, low, mid, high)
        
        return count
    
    def merge(arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1
        inv_count = 0
        
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                inv_count += (mid - left + 1)
                right += 1
        
        # Remaining elements
        while left <= mid:
            temp.append(arr[left])
            left += 1
        
        while right <= high:
            temp.append(arr[right])
            right += 1
        
        # Copy back to original array
        for i in range(len(temp)):
            arr[low + i] = temp[i]
        
        return inv_count
    
    return merge_sort(arr, 0, len(arr) - 1)

arr=[5,3,2,4,1]
print(countInversions(arr))