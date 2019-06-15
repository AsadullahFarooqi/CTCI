class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def create_list(l):
    r = Node(l[0])
    temp = r
    for i in l[1:]:
        t = Node(i)
        temp.next = t
        temp = t
    return r

def print_l(r):
    while r:
        print(r.val)
        r = r.next
    return

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

def recursive(root,k):
    # Get to end of the linked list and recurlivly keep track of the elements
    # and return 

    if not root.next:
        return root.val,1
    s,kth = recursive(root.next,k)
    if kth == k:
        return s, kth
    
    return root, kth+1


def iteratively(root, kth):
    # iterate on the list with two pointers with the kth difference by the same pace 
    # so when the 2nd pointer hits the end the first one will be on kth 
    
    i = 1
    temp = root
    while i <= kth:
        temp = temp.next
        i += 1

    k = root
    while temp:
        temp = temp.next
        k = k.next
    return k


if __name__ == '__main__':
    l = [23, 53, 66, 99, 90, 49, 12]
    r = create_list(l)
    # print(recursive(r, 2)[0].val)
    print(iteratively(r, 2).val)
