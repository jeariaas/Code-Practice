from collections import deque
from typing import List

#Input: 1 2 4 x 7 x x 5 x x 3 x 6 x x

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE

    def bfs(root):
        if not root:
            return []
        
        queue = deque([root])
        counter = 0
        while len(queue) > 0:
            path = []
            copy = queue.copy()
            for copy_node in copy:
                path.append(copy_node.val)
                node = queue.popleft()
                queue = get_children(node, queue)
            if counter % 2 == 0:
                 result.append(path)
            else:
                 result.append(path[::-1])
            counter+=1

        return result
    
    def get_children(root, queue):
        for child in [root.left, root.right]:
                if not child:
                    continue
                queue.append(child)
                # print(child.val)
        return queue

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