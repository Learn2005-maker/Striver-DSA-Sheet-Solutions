class MinHeap:
    def __init__(self):
        self.heap=[]
        
    def heapify_up(self,i):
        while i>0:
            parent=(i-1)//2
            if self.heap[parent]<=self.heap[i]:
                break
            self.heap[parent],self.heap[i]=self.heap[i],self.heap[parent]
            i=parent
    
    def insert(self,value):
        self.heap.append(value)
        # fix heap from bottom to top
        self.heapify_up(len(self.heap)-1)
    
    def heapify_down(self,i):
        n=len(self.heap)
        
        while True:
            smallest=i
            left=2*i+1
            right=2*i+2
            
            if left < n and self.heap[left]<self.heap[smallest]:
                smallest=left  
            if right < n and self.heap[right]<self.heap[smallest]:
                smallest=right
            if smallest==i:
                break
            self.heap[i],self.heap[smallest]=self.heap[smallest],self.heap[i]
            i=smallest
    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        minimum=self.heap[0]
        # move last element to root
        self.heap[0]=self.heap.pop()   
        self.heapify_down(0)
        return minimum
    
h=MinHeap()
h.insert(10)
h.insert(5)
h.insert(2)
h.insert(7)

print(h.heap)
print(h.extract_min())
print(h.heap)