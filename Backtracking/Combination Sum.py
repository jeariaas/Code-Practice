from typing import List


#My idea is to do a recursive tree. so each branch leads to itself again.




def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    result = []


    def dfs(i, cur, total):
        
        if total == target:
            result.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return
        
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i + 1, cur, total)


    dfs(0, [], 0)
    return result

if __name__ == '__main__':
    candidates = [int(x) for x in input().split()]
    target = int(input())
    res = combination_sum(candidates, target)
    for lst in res:
        lst.sort()
    for lst in sorted(res):
        print(' '.join(map(str, lst)))