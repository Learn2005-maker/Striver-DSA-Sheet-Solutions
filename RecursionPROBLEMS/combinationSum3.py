# Time complexity: (9 choose k) * k or O(9 choose k) because we are generating all the combinations of k numbers from 1 to 9 and for each combination we are 
# copying the current combination to the answer list.
def combination3(start,k,n,combo,cursum,ans):
    if len(combo)==k:
        if cursum==n:
            ans.append(combo[:])
        return
    for i in range(start,10):
        combo.append(i)
        combination3(i+1,k,n,combo,cursum+i,ans)
        combo.pop()
        
k=3
n=8
ans=[]
combination3(1,k,n,[],0,ans)
print(ans)