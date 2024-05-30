from typing import List

def permutations(letters: str) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE

    def dfs(start_index, path, used):
        if start_index == len(letters):
            result.append(''.join(path))
            return
        for index, character in enumerate(letters):
            if used[index]:
                continue
            used[index] = True
            path.append(character)
            dfs(start_index+1, path, used)
            path.pop()
            used[index] = False

    result = []
    dfs(0, [], [False]*len(letters))
    print(result)
    return []

if __name__ == '__main__':
    letters = input()
    res = permutations(letters)
    for line in sorted(res):
        print(line)