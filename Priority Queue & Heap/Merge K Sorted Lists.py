from typing import List
from heapq import heapify, heappop, heappush

def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    res = []
    heap = []
    for list in lists:
        heappush(heap, (list[0], list, 0))
    print(heap)

    while heap:
        val, current_list, head_index = heappop(heap)
        print(val, current_list, head_index)
        res.append(val)
        head_index +=1
        if head_index < len(current_list):
            heappush(heap, (current_list[head_index], current_list, head_index))

    return res

if __name__ == '__main__':
    lists = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = merge_k_sorted_lists(lists)
    print(' '.join(map(str, res)))