from math import inf

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root: Node) -> bool: #return value is a boolean true/false
    # WRITE YOUR BRILLIANT CODE HERE

        def validate(root, min_val, max_value):

            if not root:
                 return True
            elif (root.val != None and root.val >= max_value) or (root.val != None and root.val <= min_val):
                 

            return
        
        return validate(root, -inf, inf)

    

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
    res = valid_bst(root)
    print('true' if res else 'false')