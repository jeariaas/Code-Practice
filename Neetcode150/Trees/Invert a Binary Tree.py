from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
    if not root: 
         return None
    print(root.val)
    root.left, root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root

    '''
    Step 1
    We must always check if the node we're on is None. This means that the node itself is None not its left or right children

    Step 2
    We need to swap left and right. We use this x,y = y,x syntax because thats how you do it python. It does not run into temporary object problems

    Step 3
    This is the dfs part. We go all the way to the left of the tree until we reach a None node. Then we back up to the previous Node and go the right subtree. Repeat until we return until the top most node.

    Step 4
    Return the root, this will return the topmost Node because it will return itself back into the topmost Node.
    
    '''