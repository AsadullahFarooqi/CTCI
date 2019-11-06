def in_order_recursive(node, l):
    if node != None:
        in_order_recursive(node.left, l)
        l.append(node.val)
        in_order_recursive(node.right, l)
    return l

def valid_bst_by_in_order_walk(root):
    l = in_order_recursive(root, [])
    if not len(l):
        return True
    for i in range(1, len(l)):
        if l[i] < l[i-1]: return False

    return True

last_element = None
def in_order_walk_solution(node):
    if node != None:
        in_order_walk_solution(node.left)
        if last_element > nod.val:
            return False
        last_element = node.val
        in_order_walk_solution(node.right)
    return True