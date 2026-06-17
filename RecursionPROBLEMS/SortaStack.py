def insertSorted(stack,x):
    if not stack or stack[-1]<=x:
        stack.append(x)
        return
        
        
    temp=stack.pop()
    insertSorted(stack,x)
    stack.append(temp)
        


def sortStack(stack):
    if not stack:
        return
    x=stack.pop()
    sortStack(stack)
    insertSorted(stack,x)        
    
stack=[4,1,3,2]
sortStack(stack)
print(stack)

# time complexity: O(n^2)
# explain in short: The function sortStack recursively pops elements from the stack until it is empty, 
# and then inserts each element back into the stack in sorted order using the insertSorted function. 
# The insertSorted function may need to pop multiple elements to find the correct position for the new element, 
# leading to a worst-case time complexity of O(n^2) when all elements are in reverse order. 
# The space complexity is O(n) due to the recursive call stack.
# space complexity: O(n)