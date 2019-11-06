def rec_sum(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0

    return n + rec_sum(n - 1)


def sum_prev_to_i(nums, i):
    if i <= 1:
        return sum_prev_to_i(nums, i + 1)
    elif i >= len(nums):
        return nums
    nums[i] += nums[i - 1]
    return sum_prev_to_i(nums, i + 1)


def pow(x, y):
    if y == 0:
        return 1
    elif x == 1:
        return x
    return x * pow(x, y - 1)


def tower_of_hanoi(source, des, e_tower, disks):
    if disks <= 0:
        # print("Disk-{} From {} To {}".format(disks, source, des))
        return
    # shift n-1 disks from A to B
    print("goes in", disks)
    tower_of_hanoi(source, e_tower, des, disks-1)
    print("first entry")
    print("Move Disk-{} From {} To {}".format(disks, source, des))
    tower_of_hanoi(e_tower, des, source, disks-1)
#tower_of_hanoi("S", "D", "E", 3)


def tower_of_hanoi_num_of_moves(n):
    prev = 0
    for i in range(1, n + 1):
        i += prev
        print(i)
        prev += i
# tower_of_hanoi_num_of_moves(9)
# @cassy#4365

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_list(l):
    r = ListNode(l[0])
    temp = r
    for i in l[1:]:
        t = ListNode(i)
        temp.next = t
        temp = t
    return r

def print_linked_list(head):
    if head != None:
        print_linked_list(head.next)
        print(head.val, end=" ")
r = create_list([3,5,2,1])
# print_linked_list(r)


def buble_sort_recursiv(ls, length):
    if length <= 0:
        return
    for i in range(length-1):
        if ls[i] > ls[i+1]:
            ls[i], ls[i+1] = ls[i+1],ls[i]
    buble_sort_recursiv(ls,length-1)
l = [3,5,2,1]
buble_sort_recursiv(l, 4)
print(l)

def binary_search_recursiv(ls, start, mid, end, value):
  if ls[mid] == value:
    print(mid, value)
    return True
  elif start >= end:
    print("sorry couldn't find it")
    return False
  elif ls[mid] > value:
    end = mid-1
    mid = (start + end) // 2
    binary_search_recursiv(ls, start, mid, end, value)

  else:
    start = mid+1
    mid = (start + end) // 2
    binary_search_recursiv(ls, start, mid, end, value)

ls = [3, 6, 9, 10, 12, 14, 15, 17, 20, 22]
binary_search_recursiv(ls, 0, 0+len(ls)-1, len(ls)-1, 16)
