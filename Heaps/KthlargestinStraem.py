import heapq

class KthLargest:
    def __init__(self, k: int, nums):
        self.k=k
        self.heap=[]

        for i in range(len(nums)):
            heapq.heappush(self.heap,nums[i])

            if len(self.heap)>k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


obj=KthLargest(3,[4,5,8,2])

print(obj.add(3))
print(obj.add(5))
obj.add(10)
obj.add(9)
# time complexcity:O(n log k) and S.c :O(k)