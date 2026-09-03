val = [100,60,100,200]
wt = [20,10,50,10] 
capacity=50
totalVal=0

items=[]
for i,j in zip(val,wt):
    items.append((i,j))
items.sort(key= lambda item :item[0]/item[1],reverse=True)

print(items)

for i in range(len(items)):
    if items[i][1]<=capacity:
        totalVal+=items[i][0]
        capacity-=items[i][1]
    else:
        totalVal+=(items[i][0]/items[i][1])*capacity
        break


print(totalVal)

# Time complecity: O(n logn)





