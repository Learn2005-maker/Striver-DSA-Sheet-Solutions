
def maxMeetings(start,end):
  n=len(start)
  meetings=[]
  for i in range(n):
    meetings.append((end[i],start[i],i+1))

  meetings.sort() 
  print(meetings)# Based on ending time.
  count=1
  freeTime=meetings[0][0]
  order=[]
  order.append(meetings[0][2])
  for end_time,start_time,meeting_no in meetings:
    if start_time>freeTime:
      count+=1
      order.append(meeting_no)
      freeTime=end_time
  return (order , f" count :{count}")



start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]


print(maxMeetings(start,end))
