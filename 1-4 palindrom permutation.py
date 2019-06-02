def solution1(s):
    # check if more then one element 
    # the dictionary can also be used for such a task but i think list is good
    counts = [0] * 26
    for i in s:
        counts[ord(i)-ord('a')] += 1
    od_count = 0
    for j in counts:
        if j % 2:
            od_count += 1

    return od_count < 2

def solution2(s):
    # using sorting
    if len(s) < 3:
        return False
    s = sorted(s)
    odd_count = 0
    i = 1
    c = 1
    while i < len(s):
        if s[i-1] != s[i]:
            odd_count += c%2
            c = 1
            i += 1
            continue
        c += 1
        i += 1
    return odd_count < 2


if __name__ == '__main__':
    print(solution2("dasad"))