from collections import deque
from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE

    def bfs(root):
        queue = deque([root])
        while len(queue) > 0:
            node = queue.popleft()
            result.append(node.val)
            for child in [node.left, node.right]:
                if not child:
                    continue
                queue.append(child)
                print(child.val)
        return

    result = []
    bfs(root)
    return result

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = level_order_traversal(root)
    for row in res:
        print(' '.join(map(str, row)))