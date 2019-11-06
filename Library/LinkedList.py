from Nodes import ListNode
        
class LinkedList:

    def __init__(self):

    def push(self, root, value):
        """Summary

        Args:
            root (TYPE): Description
            value (TYPE): Description

        Returns:
            TYPE: Description
        """
        temp = root
        while temp.next:
            temp = temp.next
        temp.next = ListNode(value)
        return root

    def pop(self, root):
        """Summary

        Args:
            root (TYPE): Description

        Returns:
            TYPE: Description
        """
        temp = root
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None
        return root

    def insert(self, value, root=None, index=None):
        """Summary

        """
        if not root:
            return ListNode(value)
        elif not index:
            return push(root, value)
        i = 0
        temp = root
        while i <= index - 1:
            i += 1
            temp = temp.next

        b = ListNode(value)
        b.next = temp.next
        temp.next = b
        return root

    def print_list(self, root):
        temp = root
        while temp:
            if not temp.next:
                print(temp.val)
                break
            print(temp.val, end=" -> ")
            temp = temp.next
        print()

    def delete(self, root, value=None, index=None):
        """Summary

        """
        temp = root
        while temp.val != value:
            temp = temp.next
        return root

    def create_list(self, l):
        """Summary
        This method will create a linkedlist from given partition 
        """
        r = ListNode(l[0])
        temp = r
        for i in l[1:]:
            t = ListNode(i)
            temp.next = t
            temp = t
        return r
