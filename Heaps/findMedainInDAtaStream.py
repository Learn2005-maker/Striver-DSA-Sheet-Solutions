

# T.c: O(nlog n)
import heapq

class MedianFinder:

    def __init__(self):
        self.right=[] # min heap
        self.left=[]  # max heap (-)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left,-num)
        if self.right and (-self.left[0])>self.right[0]:
            val=-heapq.heappop(self.left)
            heapq.heappush(self.right,val)
        # balancing for odd and even elements
        if len(self.left)>len(self.right)+1:
            heapq.heappush(self.right,-heapq.heappop(self.left))
        elif len(self.right)>len(self.left):
            heapq.heappush(self.left,-heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left)>len(self.right):
            return float(-self.left[0])
        return (-self.left[0]+self.right[0])/2.0