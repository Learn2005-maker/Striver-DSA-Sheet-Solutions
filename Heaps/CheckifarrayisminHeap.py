# T.c :O(n) for to check minheap and maxheap

def ismin_heap(arr):
    n=len(arr)
    
    for i in range(n//2):
        left=2*i+1
        right=2*i+2
        
        if left < n and arr[i]>arr[left]:
            return False
        if right < n and arr[i]>arr[right]:
            return False
        
        return True
            
arr=[10,15,14,15,30]

print(ismin_heap(arr))


def ismax_heap(arr):
    n=len(arr)
    
    for i in range(n//2):
        left=2*i+1
        right=2*i+2
        
        if left < n and arr[i]<arr[left]:
            return False
        if right < n and arr[i]<arr[right]:
            return False
        
        return True
            
arr=[10,15,14,15,30]

print(ismax_heap(arr))
         