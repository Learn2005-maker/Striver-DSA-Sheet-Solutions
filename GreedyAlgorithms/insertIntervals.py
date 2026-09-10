intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

res=[]

n=len(intervals)

i=0
while i < n and intervals[i][1]<newInterval[0]:
    res.append(intervals[i])
    i+=1

while i<n and intervals[i][0]<=newInterval[1]:
    newInterval[0]=min(newInterval[0],intervals[i][0])
    newInterval[1]=max(newInterval[1],intervals[i][1])
    i+=1
res.append(newInterval)

while i<n:
    res.append(intervals[i])
    i+=1

print(res)