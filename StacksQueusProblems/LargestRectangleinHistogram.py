#Largest Rectangle in Histrogram
# T.c:O(5n) and S.c :O(2n)
def findNse(arr):
    n=len(arr)
    stack=[]
    nse=[n]*n
    for i in range(len(arr)-1,-1,-1):
        while stack and arr[stack[-1]]>=arr[i]:
            stack.pop()
        if stack:
            nse[i]=stack[-1]
        stack.append(i)
    return  nse
def findPse(arr):
    n=len(arr)
    stack=[]
    pse=[-1]*n
    for i in range(len(arr)):
        while stack and arr[stack[-1]]>arr[i]:
            stack.pop()
        if stack:
            pse[i]=stack[-1]
        stack.append(i)
    return  pse         

arr= [2,1,5,6,2,3]
nse=findNse(arr)
pse=findPse(arr)
max_area=0
for i in range(len(arr)):
    max_area=max(max_area,arr[i]*(nse[i]-pse[i]-1))

print(max_area)






     

arr= [2,1,5,6,2,3]
# t.c:O(2n) ans s.c:O(n)
max_area=0
stack=[]
n=len(arr)
for i in range(len(arr)):
    while stack and arr[stack[-1]]>arr[i]:
        element=stack[-1]
        stack.pop()
        nse=i
        pse=stack[-1] if stack else -1
        max_area=max(max_area,arr[element]*(nse-pse-1))
    stack.append(i)
while stack:
    element=stack[-1]
    stack.pop()
    nse=n
    pse=stack[-1] if stack else -1 
    max_area=max(max_area,arr[element]*(nse-pse-1))
print(max_area)


