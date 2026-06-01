class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(low, high):
            if low >= high:
                return 0
            
            mid = (low + high) // 2
            count = 0
            
            count += merge_sort(low, mid)
            count += merge_sort(mid + 1, high)
            count += count_pairs(low, mid, high)
            merge(low, mid, high)
            
            return count
        
        def count_pairs(low, mid, high):
            count = 0
            j = mid + 1
            
            for i in range(low, mid + 1):
                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))
            
            return count
        
        def merge(low, mid, high):
            temp = []
            left = low
            right = mid + 1
            
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            
            while left <= mid:
                temp.append(nums[left])
                left += 1
            
            while right <= high:
                temp.append(nums[right])
                right += 1
            
            for i in range(len(temp)):
                nums[low + i] = temp[i]
        
        return merge_sort(0, len(nums) - 1)
    
    
nums=[1,3,2,3,1]
solution = Solution()    
print(solution.reversePairs(nums))
        