def first_common_ancestor(r, n, m):
    if root == None:
        return None

    if n.val <= r.val and m.val > r.val:
        return r

    elif n.val > r.val:
        return first_common_ancestor(r.right, n, m)
    else:
        return first_common_ancestor(r.left, n, m)