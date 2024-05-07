# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['4','6'],
  '4' : ['3', '8'],
  '3' : [],
  '8' : [],
  '6' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

tree


# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')