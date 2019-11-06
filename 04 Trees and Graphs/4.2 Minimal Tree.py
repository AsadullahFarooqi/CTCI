class Node:

    def __init__(self, value):
        self.parent = None
        self.val = value
        self.left = None
        self.right = None

def minal_tree(A):
    return create_bst(A, 0, len(A)-1)

def create_bst(arr, start, end):
    if end < start:
        return None
    mid = (start+end) // 2
    node = Node(arr[mid])
    node.left = create_bst(arr, start, mid-1)
    node.right = create_bst(arr, mid+1, end)
    return node

def in_order_recursive(root):
    if root != None:
        print(root.val)
        in_order_recursive(root.left)
        in_order_recursive(root.right)


if __name__ == '__main__':
    a = [51, 53, 54, 55, 57, 3, 20, 33, 34, 45, 83, 85, 98]
    r = minal_tree(sorted(a))
    print(in_order_recursive(r))