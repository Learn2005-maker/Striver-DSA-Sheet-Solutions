cardPoints = [1,2,3,4,5,6,1]
k = 3

n=len(cardPoints)

max_sum=0
l_sum=0
r_sum=0

for i in range(k):
    l_sum+=cardPoints[i]
    max_sum=l_sum
r_index=n-1
for i in range(k-1,-1,-1):
    l_sum-=cardPoints[i]
    r_sum+=cardPoints[r_index]
    r_index-=1
    max_sum=max(max_sum,l_sum+r_sum)

print(max_sum)    


# t.c:O(2k) s.c :O(1)