def canJump(nums):
  maxIndex=0

  for i in range(len(nums)):
    if i>maxIndex:
      return False
      maxIndex=max(maxIndex,i+nums[i])
    return True


nums=[2,3,1,1,4]

print(canJump(nums))
      
      