class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traversal(root: Node,) -> int: #need to return the node.val of a the ancestor
    # WRITE YOUR BRILLIANT CODE HERE

    def dfs(root):
        if not root:
            return
        print(root.val)
        for child in [root.left, root.right]:
            dfs(child)
        
    return dfs(root)

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    bst = build_tree(iter(input().split()), int)
    res = traversal(bst)
    print(res)