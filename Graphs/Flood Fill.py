from typing import List
from collections import deque

'''
input:
2
4
5
5
0 1 3 4 1
3 8 8 3 3
6 7 8 8 3
12 2 8 9 1
12 3 1 3 2
'''
def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    def bfs():
        col_delta = [0,1,0,-1]
        row_delta = [-1,0,1,0]
        original = image[r][c]
        visited = [[r,c]]
        queue = deque([[r,c]])
        xlen, ylen = len(image), len(image[0])
        
        while len(queue) > 0:
            n = len(queue)
            for n in range(n):
                vertex = queue.popleft()
                vertexRow, vertexCol = vertex[0], vertex[1]
                for number in range(4):
                    rowcoor = vertexRow + row_delta[number] # number = 0: xcoor = 2, ycoor = 3: image[3][2] = 
                    colcoor = vertexCol + col_delta[number]
                    if 0 <= rowcoor < xlen and 0 <= colcoor < ylen:
                        if image[rowcoor][colcoor] == original and [rowcoor,colcoor] not in visited:
                            # print("rowcoor", rowcoor, "colcoor", colcoor, "answer", image[rowcoor][colcoor]) #[row][col]
                            queue.append([rowcoor,colcoor])
                            visited.append([rowcoor,colcoor])
        for x, y in visited:
            image[x][y] = replacement
        return image
    
    return bfs()

if __name__ == '__main__':
    r = int(input())
    c = int(input())
    replacement = int(input())
    image = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = flood_fill(r, c, replacement, image)
    for row in res:
        print(' '.join(map(str, row)))