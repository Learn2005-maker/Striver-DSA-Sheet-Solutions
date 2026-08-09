class Solution:
    def sumSubarrayMins(arr) -> int:
        def findNge(arr):
            n=len(arr)
            nge=[0]*n
            stack=[]
            # Iterate from right to left to find Next Strictly Less Element (NSLE)
            for i in range(n-1,-1,-1):
                # Pop elements from stack that are >= current element
                while stack and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                if stack:
                    # If stack is not empty, top is NSLE
                    nge[i]=stack[-1]
                else:
                    # No NSLE to the right, default to n
                    nge[i]=n
                stack.append(i)        
            return nge        

        def findPSEE(arr):
            n=len(arr)
            psee=[0]*n
            stack=[]
            # Iterate from left to right to find Previous Smaller or Equal Element (PSEE)
            for i in range(n):
                # Pop elements from stack that are > current element
                while stack and arr[stack[-1]]>arr[i]:
                    stack.pop()
                if stack:
                    # If stack is not empty, top is PSEE
                    psee[i]=stack[-1]
                else:
                    # No PSEE to the left, default to -1
                    psee[i]=-1
                stack.append(i)    
            return psee
        
        n=len(arr)
        # Calculate NSLE for all elements
        nge=findNge(arr)
        # Calculate PSEE for all elements
        psee=findPSEE(arr)
        
        total=0
        mod=10**9+7
        
        # Iterate through each element to calculate its contribution as a minimum
        for i in range(n):
            # Number of elements to the left (including arr[i]) for which arr[i] is the minimum
            left = i - psee[i]
            # Number of elements to the right (including arr[i]) for which arr[i] is the minimum
            right = nge[i] - i
            
            # Add the contribution of arr[i] to the total sum
            total=(total + left * right * arr[i]) % mod
            
        return total