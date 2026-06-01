
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.
intervals=[[1,3],[2,4],[8,10],[8,12]]
n= len(intervals)
if not intervals:
    print([]) 
intervals.sort()
result = [intervals[0]]
for i in range(1, n):
    current_start, current_end = intervals[i]
    last_start, last_end = result[-1]

    if current_start <= last_end:
        result[-1][1] = max(last_end, current_end)
    else:
        result.append(intervals[i])
        
print(result)        