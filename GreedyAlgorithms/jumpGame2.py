def jump2(index,jumps):
  if index>=len(nums)-1:
    return jumps
  minI=float("inf")

  for i in range(1,nums[index]+1):
    minI=min(minI,jump2(index+i,jumps+1,nums))
  return minI
  


nums = [2,3,1,1,4]
print(jump2(0,0,nums))

# Time complexity: O(N^N) and it excecds TLE in leetcode


nums = [2,3,1,4,1,1,1,2]
n=len(nums)


l=0
r=0

jumps=0
# while is to check the farthest range. ( did you reach)   
# Time complxity:O(n)
while r<n-1:
    farthest=0

    for i in range(l,r+1):
        farthest=max(i+nums[i],farthest)
    l=r+1
    r=farthest
    jumps+=1

print(jumps)




