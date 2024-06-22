from typing import List
from collections import deque

# 4
# 1 2
# 0 2 3
# 0 1
# 1
# 0
# 3

def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE

    def bfs(root, target):
        
        queue = deque([root])
        visited = set()
        level = 0
        while len(queue) > 0:
            node = queue.popleft()
            if node == target:
                return level
            if node in visited:
                continue
            visited.add(node)
            for neighbors in graph[node]:
                print(neighbors)
                queue.append(neighbors)
            level +=1

    return bfs(a, b)

if __name__ == '__main__':
    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    a = int(input())
    b = int(input())
    res = shortest_path(graph, a, b)
    print(res)