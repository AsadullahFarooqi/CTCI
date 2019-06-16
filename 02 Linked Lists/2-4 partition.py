from LinkedList import LinkedList

def solution(r, x):
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
    """

if __name__ == '__main__':
    l = [53, 66, 99, 90, 49, 12, 23, 10]
    r = LinkedList().create_list(l)
    
    LinkedList().print_list(solution(r, 53))