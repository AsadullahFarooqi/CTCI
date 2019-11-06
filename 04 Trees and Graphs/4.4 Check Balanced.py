def recursive_check(node):
    if node == None:
        return -1

    left = recursive_check(node.left)
    right = recursive_check(node.right)

    if left == float("-inf") or right == float("-inf") or abs(right-left) > 1:
        return float("-inf")

    return max(left, right) + 1

def check_balanced(root):
    return not recursive_check(root) == float("-inf")
