       
def possibleToColor(node,color,edges,colors):
    for u,v in edges:
        if u==node and colors[v]==color:
            return False
        if v==node and colors[u]==color:
            return False    
    return True    
 
def graphColouring(node,n,m,edges,colors):
    # If all nodes are coloured
    if node==n:
        return True
    for color in range(1,m+1):
        # If current color is valid
        if possibleToColor(node,color,edges,colors):
            colors[node]=color
            # Recurse
            if graphColouring(node+1,n,m,edges,colors)==True:
                return True
            colors[node]=0    
    return False        
        
N = 4
M = 3 
E = 5
Edges = [ (0, 1) , (1, 2) , (2, 3) , (3, 0) , (0, 2) ]
colors=[0]*N
if graphColouring(0,N,M,Edges,colors):
    print("Possible")
    print("Color Assignment:",colors)
else:
    print("Not Possible")

# Time complexity: O(M^N) where M is the number of colors and N is the number of nodes.
# Space complexity: O(N) for the colors array and recursion stack.
2


# If you want to use adjacency list representation of the graph, 
# you can modify the code as follows:


# graph = {
#     0: [1,2,3],
#     1: [0,2],
#     2: [0,1,3],
#     3: [0,2]
# }

# for neighbor in graph[node]:
#     if colors[neighbor] == color
#         return False