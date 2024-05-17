# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”

# Input
#     bst: a binary tree representing the existing BST.
#     p: the value of node p as described in the question
#     q: the value of node q as described in the question

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca_on_bst(bst: Node, p: int, q: int) -> int: #need to return the node.val of a the ancestor
    # WRITE YOUR BRILLIANT CODE HERE

    def ancestor(bst, p, q):
        if p > bst.val and q > bst.val:
            return ancestor(bst.right, p, q)
        elif p < bst.val and q < bst.val:
            return ancestor(bst.left, p, q)
        else:
            return bst.val
    return ancestor(bst, p, q)

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
    p = int(input())
    q = int(input())
    res = lca_on_bst(bst, p, q)
    print(res)