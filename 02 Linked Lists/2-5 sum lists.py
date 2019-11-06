from Library import LinkedList

def solution_iterative(A,B):
    """
    Steps that this algorithm takes
    1 - iterate through list A and appends each node value of the 
        list to string type var a 
    2 - iterate through list B and appends each node value of the 
        list to string type var b 
    3 - convert the a,b to ints and add the results store in c
    4 - call the LinkedList function create_list to create a new 
        list from the digits of c and return root of the list
    Args:
        A (Linked List): first number each node is a digit
        B (Linked List): second number each node is a digit
    
    Returns:
        Linked List: result of the sum converted to linked list
            and each digit is a node
    """
    a = ""
    while A:
        a += str(A.val)
        A = A.next

    b = ""
    
    while B:
        b += str(B.val)
        B = B.next

    c = [int(i) for i in str(int(a) + int(b))]

    r = LinkedList().create_list(c)
    return r

if __name__ == '__main__':
    a = LinkedList().create_list([3, 3, 6])
    b = LinkedList().create_list([2, 5, 6])
    LinkedList().print_list(solution_iterative(a,b))
