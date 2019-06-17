from LinkedList import LinkedList
def solution_iterative(root):
    ans = ""
    while root:
        ans += str(root.val)
        root = root.next
    return ans == ans[::-1]

if __name__ == '__main__':
    l = [1,0]
    r = LinkedList().create_list(l)
    # print(recursive(r, 2)[0].val)
    print(solution_iterative(r))
