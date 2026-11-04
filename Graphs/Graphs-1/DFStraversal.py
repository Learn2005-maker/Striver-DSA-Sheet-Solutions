
def dfs(node,adj,vis,ls):
    vis[node]=1
    ls.append(node)
    for neighbor in adj[node]:
        if not vis[neighbor]:
            dfs(neighbor,adj,vis,ls)
    
    
# it visits all components, including disconnected nodes. # 
def dfsGraph(V,adj):
    vis=[0]*V
    
    lis=[]
    for i in range(V):
        if not vis[i]:
            dfs(i,adj,vis,lis)
    return lis



n=5
# Adjacency list for undirected graph.
adj=[[] for _ in range(n)]
m=int(input("enter number of edges:"))
for i in range(m):
    u=int(input("enter u:"))
    v=int(input("enter v:"))

    adj[u].append(v)

    adj[v].append(u)
print(adj)


print(dfsGraph(n, adj))
