class Node:
    """docstring for ClassName"""
    def __init__(self, value):
        """Summary

        Args:
            value (TYPE): Description
        """
        self.val = value
        self.next = None
        
class LinkedList:

    """Summary

    Attributes:
        next (TYPE): Description
        val (TYPE): Description
    """

    def __init__(self):
        """Summary

        Args:
            value (TYPE): Description
        """

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
        temp.next = Node(value)
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

        Args:
            value (TYPE): Description
            root (None, optional): Description
            index (None, optional): Description

        Returns:
            TYPE: Description
        """
        if not root:
            return Node(value)
        elif not index:
            return push(root, value)
        i = 0
        temp = root
        while i < index - 1:
            i += 1
            temp = temp.next

        b = Node(value)
        b.next = temp.next
        temp.next = b
        return root

    def print_list(self, root):
        """Summary

        Args:
            root (TYPE): Description
        """
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

        Args:
            root (TYPE): Description
            value (None, optional): Description
            index (None, optional): Description

        Returns:
            TYPE: Description
        """
        temp = root
        while temp.val != value:
            temp = temp.next
        return root

    def create_list(self, l):
        """Summary
        This method will create a linkedlist from given partition 
        Args:
            l (TYPE): Description

        Returns:
            TYPE: Description
        """
        r = Node(l[0])
        temp = r
        for i in l[1:]:
            t = Node(i)
            temp.next = t
            temp = t
        return r
