from collections import deque

def get_knight_shortest_path(x: int, y: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    rowdelta = [2,  1,  -1,  -2,  -2,  -1,   1,   2]
    coldelta = [1,  2,   2,   1,  -1,  -2,  -2,  -1]

    def bfs():
        moves = 0
        queue = deque([[0,0]])
        visited = set((0,0))
        while len(queue) > 0:
            n = len(queue)
            for n in range(n):
                node = queue.popleft()
                row = node[0]
                col = node[1]
                for n in range(len(rowdelta)):
                    newRow = row + rowdelta[n]
                    newCol = col + coldelta[n]
                    if (newRow,newCol) == (x,y):
                        return moves + 1
                    if (newRow,newCol) not in visited:
                        queue.append([newRow,newCol])
                        visited.add((newRow,newCol))
            moves +=1

    return bfs()

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    res = get_knight_shortest_path(x, y)
    print(res)