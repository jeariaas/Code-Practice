from typing import List

sensorA = [15,-4,56,10,-23]
sensorB = [14,-9,56,14,-23]

def absDiff(start_index, result) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if start_index == len(sensorA):
        ans = result
    
    result += abs(sensorA[start_index] - sensorB[start_index])
    ans = ans + absDiff(start_index + 1, result)
    return ans
    

if __name__ == '__main__':
    res = absDiff(0, 0)
    print(res)

# def permutations(letters: str) -> List[str]:
#     # WRITE YOUR BRILLIANT CODE HERE

#     def dfs(start_index, path, used):
#         if start_index == len(letters):
#             result.append(''.join(path))
#             return
#         for index, character in enumerate(letters):
#             if used[index]:
#                 continue
#             used[index] = True
#             path.append(character)
#             dfs(start_index+1, path, used)
#             path.pop()
#             used[index] = False

#     result = []
#     dfs(0, [], [False]*len(letters))
#     print(result)
#     return []

# if __name__ == '__main__':
#     letters = input()
#     res = permutations(letters)
#     for line in sorted(res):
#         print(line)