from collections import deque

class ListNode:
    """docstring for ClassName"""
    def __init__(self, value):
        self.val = value
        self.next = None

def level_order_walk_solution(tree_node):
    if tree_node == None: return

    queue = deque()
    queue.append(n)

    list_ = []

    list_.append(ListNode(n.val))
    prev = float("inf")
    while len(queue):
        tree_node = queue.leftpop()

        if tree_node.val < prev.val:
            linked_list_node = ListNode(tree_node.val)
            prev = linked_list_node

        else:
            prev.next = ListNode(tree_node.val)
            prev = prev.next

        if tree_node.left != None:
            queue.append(tree_node.left)

        if tree_node.right != None:
            queue.append(tree_node.right)

