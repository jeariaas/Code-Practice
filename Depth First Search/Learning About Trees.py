#Binary Tree Implementation
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None



#In Order Transversal
#In-order traversal visits the left branch first, then the current node, and finally the right branch. 
#The diagram below shows the traversal order of an in-order traversal on a binary tree.
def in_order_traversal(root: Node):
    if root is not None:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)

#Pre Order Transversal
#Pre-order traversal visits the current node first, then the left subtree, and finally the right subtree. 
#The diagram below shows the traversal order of a pre-order traversal on a binary tree.
def pre_order_traversal(root: Node):
    if root is not None:
        print(root.val)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

#Post-order traversal visits the left subtree first, then the right subtree, and finally the current node. 
#The diagram below shows the traversal order of a post-order traversal on a binary tree.
def post_order_traversal(root: Node):
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val)

#How Algomonster Encodes Non-Binary Trees
class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)