# A "Binary Search Tree", or BST, is a rooted binary tree with the value of each internal node 
# being greater than all the values in the respective node's left subtree and less than the ones in its right subtree.

class Node:
    def __init__(self, val, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right

def find(tree, val):
    if tree is None:
        return False
    if tree.val == val:
        return True
    elif tree.val < val:
        return find(tree.right, val)
    else:
        return find(tree.left, val)

def insert(tree, val):
    if tree is None:
        return Node(val)
    if tree.val < val:
        tree.right = insert(tree.right, val)
    elif tree.val > val:
        tree.left = insert(tree.left, val)
    return tree