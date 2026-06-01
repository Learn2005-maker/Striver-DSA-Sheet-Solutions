
# count frequency of element


nums=[1,1,1,2,2,3]
dici={}

for i in nums:
    if i not in dici:
        dici[i]=1
    else:
        dici[i]+=1
        
print(dici)            