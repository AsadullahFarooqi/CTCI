from Library import LinkedList 
def solution(r):
    temp_r = r.next
    runner = r.next.next
    while temp_r != runner:
        runner = runner.next.next
        temp_r = temp_r.next

    temp_r = r
    while temp_r != runner:
        temp_r = temp_r.next
        runner = runner.next

    return temp_r

if __name__ == '__main__':
    a = LinkedList().create_list([3, 6, 8, 9, 2, 5, 6,7,3,2,4])
    i = 0
    r = a
    while i < 6:
        i += 1
        r = r.next
    e = a
    while e.next != None:
        e = e.next
    e.next = r

    print(solution(a).val)