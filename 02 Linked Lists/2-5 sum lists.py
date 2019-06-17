from LinkedList import LinkedList

def solution_iterative(A,B):
    a = ""
    while A:
        a += str(A.val)
        A = A.next

    b = ""
    
    while B:
        b += str(B.val)
        B = B.next

    c = str(int(a) + int(b))

    r = LinkedList().create_list(c)
    return r

if __name__ == '__main__':
    a = LinkedList().create_list([3, 3, 6])
    b = LinkedList().create_list([2, 5, 6])
    LinkedList().print_list(solution_iterative(a,b))
