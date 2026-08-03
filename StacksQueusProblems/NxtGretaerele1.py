# step1:find NGE in nums2
# step2:built the ans from nums1
# nums2 contains all the numbers.
# nums1 is a subset of nums2.
# First, compute the Next Greater Element for every element in nums2.
# Store the result in a dictionary (hash map).
# Then, answer each query in nums1 by looking it up in the dictionary
def Nge(nums1,nums2):
    n=len(nums2)
    nge={}
    stack=[]
    for i in range(n-1,-1,-1):
        while stack and stack[-1]<=nums2[i]:
            stack.pop()
        if len(stack)==0:
            nge[nums2[i]]=-1
        else:
            nge[nums2[i]]=stack[-1]
        stack.append(nums2[i])   
    ans=[]
    for num in nums1:
        ans.append(nge[num])
    return ans        
nums1=[4,1,2]
nums2=[1,3,4,2]
result=Nge(nums1,nums2)
print(result)
