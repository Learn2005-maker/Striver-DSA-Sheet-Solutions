

def dfs(node,adj,visL):
    visL[node]=1

    for n in adj[node]:
        if not visL[n]:
            dfs(n,adj,visL)


def dfsGraph(V,adj):
    count=0
    visL=[0]*V
    for i in range(V):
        if not visL[i]:
            count+=1
            dfs(i,adj,visL)
    return count




isConnected = [[1,1,0],[1,1,0],[0,0,1]]
v=len(isConnected)
adjL=[[] for _ in range(v)]
for i in range(v):
    for j in range(v):
        if isConnected[i][j]==1 and i!=j:
            adjL[i].append(j)
            adjL[j].append(i)


print(dfsGraph(v,adjL))