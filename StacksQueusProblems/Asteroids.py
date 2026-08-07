asteroids=[5,6,7,9,-3,-12,4,-9,5,9,-4,3]
n=len(asteroids)
stack=[]
for i in range(n):
    if asteroids[i]>0:
        stack.append(asteroids[i])        
    else:
        while stack and stack[-1]>0 and stack[-1]<abs(asteroids[i]):
            stack.pop()
        if not stack or stack[-1]<0:
            stack.append(asteroids[i])
        elif stack and stack[-1]==abs(asteroids[i]) :
            stack.pop()
    
        
print(stack)    
# Time complexcity: O(2n)
# Space complexcity:O(n)