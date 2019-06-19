from LinkedList import LinkedList

def solution_recursive(a,b):
    """this solution is on hole i have to think about it and see 
    if i could find a way through this one 
    
    Args:
        a (TYPE): Description
        b (TYPE): Description
    
    Returns:
        TYPE: Description
    """
    if a.next == None and b.next == None:
        return a,b 
    elif a.next == None and b.next != None:
        return solution_recursive(a,b.next)
    elif a.next != None and b.next == None:
        a,b = solution_recursive(a.next,b)
    if a == b and a.next == b.next:
        print(a.val,b.val, a.next.val,b.next.val)
        return a,b
    elif a != b and a.next == b.next:
        print(a.val,b.val, a.next.val,b.next.val)
        return a.next,b.next
    # print(a.val,b.val, a.next.val,b.next.val)
    return a,b

def solution(a,b):
    """Steps
    1 - Find the length of lists
    2 - Trim the longest one so it gets equal to the short one
    3 - And then traverse each at the same pase
    4 - compare each node during walking through
    
    
    Args:
        a (Linked List): Linked List
        b (Linked List): Linked List
    """

    a_l = 0
    t_a = a 
    while t_a != None:
        a_l += 1
        t_a = t_a.next

    b_l = 0
    t_b = a 
    while t_b != None:
        b_l += 1
        t_b = t_a.next
    
    if max(a_l, b_l) == a_l:
        

if __name__ == '__main__':
    a = LinkedList().create_list([3, 6, 8, 9])
    b = LinkedList().create_list([2, 5, 6])
    c = LinkedList().create_list([7,3,2,4])
    a_e = a
    while a_e.next:
        a_e = a_e.next
    b_e = b
    while b_e.next:
        b_e = b_e.next
    a_e.next = c
    b_e.next = c
    # LinkedList().print_list(a)
    # print("done")
    # LinkedList().print_list(b)

    print(solution_recursive(a,b)[0].val)