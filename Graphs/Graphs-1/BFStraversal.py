from collections import deque
def bfsofGraph(V,adj):
    vis=[0 for _ in range(V)]
    # 0-based indexing
    vis[0]=1
    q=deque()
    q.append(0)
    bfs=[]
    while q:
        node=q.popleft()
        bfs.append(node)

        for i in adj[node]:
            if not vis[i]:
                vis[i]=1
                q.append(i)
    return bfs
n=3

# Adjacency list for undirected graph.
adj=[[] for _ in range(n)]
m=int(input("enter number of edges:"))
for i in range(m):
    u=int(input("enter u:"))
    v=int(input("enter v:"))

    adj[u].append(v)

    adj[v].append(u)
print(adj)

b=bfsofGraph(n,adj)

print(b)


# Time complexity --O(V+2E)
# space complexity --O(V)