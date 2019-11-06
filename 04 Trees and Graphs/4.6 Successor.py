def bst_min(node):
    while node.left != None:
        node = node.left
    return node

def succ(node):
    if node.right != None:
        return bst_min(node.right)
    p = node.parent
    while p != None and node == p.right:
        node = p
        p = p.parent

    return p