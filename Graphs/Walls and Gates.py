from typing import List
from collections import deque

'''
4
-9 -1 0 -9
-9 -9 -9 -1
-9 -1 -9 -1
0 -1 -9 -9
'''

# def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
#     # WRITE YOUR BRILLIANT CODE HERE
#     directions = [(1,0),(0,1),(-1,0),(0,-1)]
    
#     xlen, ylen = len(dungeon_map), len(dungeon_map[0])
#     def bfs(x,y):
#         visited = set()
#         moves = 0
#         queue = deque([[x,y]])
#         while len(queue) > 0:
#             n = len(queue)
#             for n in range(n):
#                 node = queue.popleft()
#                 nodeRow = node[0]
#                 nodeCol = node[1]
#                 for x in range(len(directions)):
#                     newRow = nodeRow + directions[x][0]
#                     newCol = nodeCol + directions[x][1]
#                     if 0 <= newRow < xlen and 0 <= newCol < ylen and (newRow,newCol) not in visited:
#                         if dungeon_map[newRow][newCol] == 0:
#                             return moves + 1
#                         queue.append([newRow, newCol])
#                         visited.add((newRow,newCol))
#             moves +=1                  
#         return moves
    
#     for x in range(len(dungeon_map)):
#         for y in range(len(dungeon_map[x])):
#             if dungeon_map[x][y] == -9:
#                 dungeon_map[x][y] = bfs(x,y)

#     return dungeon_map

def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    xlen, ylen = len(dungeon_map), len(dungeon_map[0])
    queue = deque()

    # INF = 2147483647
    # print(INF + 2)

    #Finding the locations of all the gates and adding them to the queue
    for x in range(xlen):
        for y in range(ylen):
            if dungeon_map[x][y] == 0:
                queue.append([x,y])
    print(dungeon_map)
    while queue:
        row, col = queue.popleft()
        for deltaRow, deltaCol in directions:
            newRow, newCol = row + deltaRow, col + deltaCol
            if 0 <= newRow < xlen and 0 <= newCol < ylen:
                if dungeon_map[newRow][newCol] == -9:
                    dungeon_map[newRow][newCol] = dungeon_map[row][col] + 1
                    queue.append([newRow,newCol])
                    print(dungeon_map)
    return dungeon_map

if __name__ == '__main__':
    dungeon_map = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = map_gate_distances(dungeon_map)
    for row in res:
        print(' '.join(map(str, row)))