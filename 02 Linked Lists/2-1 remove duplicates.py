def solution(root):
    # this algorithm time complexity is O(N)
    # but it takes space of O(N) too
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

def solution2(root):
    # this algorithm time complexity is O(N^2) with 2 nested loops.
    # but it takes space of O(1)
    hash_table = {}
    temp = root
    prev = None
    while temp:
        runner = temp.next
        while runner:
            if runner.next.data == temp.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        temp = temp.next

    return root

if __name__ == '__main__':
    r = None
    print(solution(r))