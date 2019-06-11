def solution1(root, kth):
    # finding the length of the linked list and then returning
    # the kth element it'll take O(2N)
    length_of_list = 0
    temp = root
    while temp:
        temp = temp.next
        length_of_list += 1

    i = 0
    while i <= length_of_list-kth and root:
        root = root.next
        i += 1
    return root.val

def recursive(root, kth, k):
    # Get to end of the linked list and recurlivly keep track of the elements
    # and return 

    pass

def iteratively(root, kth):
    # iterate on the list with two pointers with the kth difference by the same pace 
    # so when the 2nd pointer hits the end the first one will be on kth 
    pass

if __name__ == '__main__':
    main()