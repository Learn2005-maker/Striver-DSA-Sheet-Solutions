arr = [3, 4, 2, 7, 5, 8, 10, 6]
indices = [0, 5]
n=len(arr)
ans=[]
for i in indices:
    count=0
    ele=arr[i]
    for j in range(i+1,n):
        if arr[j]>ele:
            count+=1
    ans.append(count)
print(ans)            