from LinkedList import LinkedList

def solution(n):
    """
    in this solution we will replace the current node with the next node and 
    point from it to 2nd node from it
    """
    
    # this statement will check, if the given node is null then
    # it will return False
    if n == None:
        return False

    # next_ variable will hold the next node from the given node n
    next_ = n.next 
    # now have stored the data so we will change the value of n to 
    # the stored to the next node's value
    n.val = next_.val
    n.next = next_.next

    return True


if __name__ == '__main__':
    l = [23, 53, 66, 99, 90, 49, 12]
    r = LinkedList().create_list(l)
    solution(r.next.next)
    LinkedList().print_list(r)