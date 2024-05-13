class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    # WRITE YOUR BRILLIANT CODE HERE
    
    string = []

    def dfs(root):
        if not root:
            string.append('x')
            return
        string.append(root.val)
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return ' '.join(string)

    # [123xxx6xx}

def deserialize(s):
    def dfs(nodes):
        val = next(nodes)
        if val == 'x':
            return
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    return dfs(iter(s.split()))

if __name__ == '__main__':
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    def print_tree(root):
        if not root:
            yield "x"
            return
        yield str(root.val)
        yield from print_tree(root.left)
        yield from print_tree(root.right)
    root = build_tree(iter(input().split()))
    new_root = deserialize(serialize(root))
    print(' '.join(print_tree(new_root)))