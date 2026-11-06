

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
v=3
adjL=[[] for i in range(v)]
for i in range(v):
    for j in range(v):
        if isConnected[i][j]==1 and i!=j:
            adjL[i].append(j)
            adjL[j].append(i)

print(adjL)
