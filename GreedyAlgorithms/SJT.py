bt = [1, 2, 3, 4]

bt.sort()
time=0
wT=0
for i in range(len(bt)):
  wT=wT+time
  time=time+bt[i]

print(wT//len(bt))


# time complcity:O(nlogn) and space complexity:O(1)