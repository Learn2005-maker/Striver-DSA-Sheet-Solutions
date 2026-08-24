# Converting Minheap-MaxHeap
def max_heapify(arr,i,n):
    while True:
        largest=i
        left=2*i+1
        right=2*i+2
        if left < n and arr[left]>arr[largest]:
            largest=left
        if right<n and arr[right]>arr[largest]:
            largest=right
        if largest==i:
            break
        arr[i],arr[largest]=arr[largest],arr[i]
        
        i=largest
        
def min_to_max_heap(arr):
    n=len(arr)
    # start from non-leaf node index
    for i in range(n//2-1,-1,-1):
        max_heapify(arr,i,n)
        
    return arr


arr=[1,2,3,7,5]

print(min_to_max_heap(arr)) 
        