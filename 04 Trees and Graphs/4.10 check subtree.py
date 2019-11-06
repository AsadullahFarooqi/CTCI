from collections import deque

def compare_trees(r1, r2):
    if r1 == None and r2 == None:
        return True
    elif r1 == None or r2 == None:
        return False
    elif r1.val != r2.val:
        return False
    else:
        return compare_trees(r1.left, r2.left) and compare_trees(r1.right, r2.right)    


def compare_tree(r, n):

    if r != None or n != None:
        if r.val != n.val:
            return False
        compare_tree(r.left, n.left)
        compare_tree(r.right, n.right)

    return True


def search_node(r, n):
    while r != None and r.val != n.val:
        if n.val > r.val:
            r = r.right
        else:
            r = r.left

    return compare_trees(r, n)