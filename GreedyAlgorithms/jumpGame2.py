def jump2(index,jumps):
  if index>=len(nums)-1:
    return jumps
  minI=float("inf")

  for i in range(1,nums[index]+1):
    minI=min(minI,jump2(index+i,jumps+1,nums))
  return minI
  


nums = [2,3,1,1,4]
print(jump2(0,0,nums))

# time complexity: O(N^N) and it excecds TLE in leetcode


