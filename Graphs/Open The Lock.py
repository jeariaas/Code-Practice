from typing import List
from collections import deque

def num_steps(target_combo: str, trapped_combos: List[str]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    movements = [['1000'], ['0100'],['0010'],['0001']]
    queue = deque()
    




    return 0

if __name__ == '__main__':
    target_combo = input()
    trapped_combos = input().split()
    res = num_steps(target_combo, trapped_combos)
    print(res)
