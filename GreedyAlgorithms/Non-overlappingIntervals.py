
intervals = [[1,2],[2,3]]
n=len(intervals)

ans=[]
for i in range(n):
    ans.append([intervals[i][1],intervals[i][0]])


ans.sort()
count=0
lastEndTime=float("-inf")

for end ,start in ans:
    if start>=lastEndTime:
        count+=1
        lastEndTime=end
print(n-count)