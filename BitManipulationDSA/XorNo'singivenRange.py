# Time complexcity:O(R-L+1)
L=3
R=5
ans=0
for i in range(L,R+1):
    ans=ans^i
    
print(ans) 

print(3^4^5)

# This is discovered or Created Pattern:
# if N%4==1  ---->return 1
# if N%4==2  ---->return N+1
# if N%4==3 ---->return 0
# if N%4==4  ---->return 