## Detect cycles in course scheduling

def DFS(node):
    # Cycle detected.
    if visited[node] == 1:
        return False
    
    # Visit this node, explore neighbors.
    visited[node] = 1
    for nbr in G[node]:
        if visited[nbr] != 2 and not DFS(nbr):
            return False
    
    # Done visiting node.
    visited[node] = 2
    return True
        
      

# Given a graph and N vertices
visited = [0] * N # 0 => unvisited, 1 => visiting, 2 => visited
for node in graph:
    if not visited[node]:
        if DFS(node) == False:
            print("cycle detected!")
