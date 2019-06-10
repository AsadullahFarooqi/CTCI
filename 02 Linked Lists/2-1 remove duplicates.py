def solution(root):
    hash_table = {}
    temp = root
    prev = None
    while temp:
        if temp.val in hash_table:
            prev.next = temp.next
        else:
            hash_table[temp.val] = 1
        prev = temp
        temp = temp.next
    return root

if __name__ == '__main__':
    r = None
    print(solution(r))