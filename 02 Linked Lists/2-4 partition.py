from Library import LinkedList

def solution(r, x):
    # in this solution we initialize two new arrays.
    # so the technique is that we have 4 pointers 2 for left sidded list
    # where the in points to it's head and other to it's tail.
    # and just like that 2 other pointers for right sided list
    # and at the end we join the tail of left list to the head of right list head
    
    g_list_h = None
    g_list_t = None 
    s_list_h = None
    s_list_t = None

    while r:
        next_node = r.next
        r.next = None
        if r.val < x:
            if s_list_h == None:
                s_list_h = r
                s_list_t = s_list_h
            else:
                s_list_t.next = r
                s_list_t = r
        else:
            if g_list_h == None:
                g_list_h = r
                g_list_t = g_list_h
            else:
                g_list_t.next = r
                g_list_t = r

        r = next_node

    s_list_t.next = g_list_h
    
    return s_list_h

def solution2(node, x):
    """
    another bad solution to this problem is like using a bubble sort technique.
    which would be very bad because we will have to traverse on list for n times
    with nested loops.
    """

if __name__ == '__main__':
    l = [53, 66, 99, 90, 49, 12, 23, 10]
    r = LinkedList().create_list(l)
    
    LinkedList().print_list(solution(r, 53))