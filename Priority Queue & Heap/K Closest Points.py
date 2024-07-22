from typing import List
from heapq import heapify, heappop, heappush
from math import sqrt

def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    heap = []
    res = []
    for pts in points:
        heap.append((pow(pts[0],2) + pow(pts[1],2), pts))
    heapify(heap)
    
    for i in range(k):
        coord = heappop(heap)
        res.append(coord[1])
    return res

if __name__ == '__main__':
    points = [[int(x) for x in input().split()] for _ in range(int(input()))]
    k = int(input())
    res = k_closest_points(points, k)
    for row in res:
        print(' '.join(map(str, row)))

'''
input = 
3
1 1
2 2
3 3
1

4
4 4
2 4
8 1
3 -5
2
'''