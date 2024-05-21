from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> List[str]: #input is a root with children, ouput is a list of results.


    def dfs(root: Node, path: List[str]):
        #create a condition that knows when we've reached the end of the branch. This case is when all of the root's children are null.

        if all(child is None for child in root.children):
            #need to figure out how to get the exact output we want.
            result.append('->'.join(path) + '->' + str(root.val))
            # print(path)
            return

        for child in root.children:
            if child is not None:
                path.append(str(root.val))
                dfs(child, path)
                path.pop()


    result = []
    dfs(root, [])
    return result

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)