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

    def bfs(path):
        
        queue = deque()
        queue.append(0)
        visited.append(queue[0])

        while len(queue) != 0:
            for neighbors in graph[queue[0]]:
                print(neighbors)

        return

    result = []
    visited = []
    bfs([])
    return 0

if __name__ == '__main__':
    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    a = int(input())
    b = int(input())
    res = shortest_path(graph, a, b)
    print(res)