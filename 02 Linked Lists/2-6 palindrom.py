from LinkedList import LinkedList
def solution_iterative(root):
    ans = ""
    while root:
        ans += str(root.val)
        root = root.next
    return ans == ans[::-1]

def solution2(root):
    # the other way would be to make a reversed copy of the list 
    # and iterate through both lists at the same phase and compare the
    # elements if they aren't equal return False other wise True.

if __name__ == '__main__':
    l = [1,0]
    r = LinkedList().create_list(l)
    # print(recursive(r, 2)[0].val)
    print(solution_iterative(r))
