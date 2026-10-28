n=5
m=5
# Adjacency matrix
adj=[[0]*(n+1) for _ in range(m+1)]


for i in range(m+1):
    u=int(input("enter u:"))
    v=int(input("enter v:"))

    adj[u][v]=1
    adj[v][u]=1
print(adj)
# Space complexity --O(n^2)



n=3
m=3
# Adjacency list for undirected graph.
adj=[[] for _ in range(m+1)]

print(adj)
for i in range(m):
    u=int(input("enter u:"))
    v=int(input("enter v:"))

    adj[u].append(v)

    adj[v].append(u)
print(adj)
# Space complexity --O(2E) 
# for directed graph the s.c  is O(E)



n=3
m=3
# Adjacency list for weighted undirected graph.
adj=[[] for _ in range(m+1)]

print(adj)
for i in range(m):
    u=int(input("enter u:"))
    v=int(input("enter v:"))
    w=int(input("enter weight:"))
    adj[u].append((v,w))

    adj[v].append((u,w))
print(adj)

