def solution1(a, b):
    # using sort
    if len(a) != len(b):
        return False
    a = sorted(a)
    b = sorted(b)

    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def solution2(a, b):
    # using hash table to count charecters
    if len(a) != len(b):
        return False
    hash_table = {}
    for i in range(len(a)):
        if a[i] in hash_table:
            hash_table[a[i]] += 1
        hash_table[a[i]] = 1
        if b[i] in hash_table:
            hash_table[b[i]] += 1
        hash_table[b[i]] = 1

    for i in hash_table.values():
        if i > 1 and i % 2:
            return False
    return True

def solution3(a, b):
    # brute force way
    if len(a) != len(b):
        return False

    for i in a:
        if a.count(i) != b.count(i):
            return False

    return True

def solution4(a, b):
    # remove each chr from b a little like a brute force approach
    if len(a) != len(b):
        return False
    b = list(b)
    for i in a:
        try:
            b.remove(i)
        except:
            return False
    return not bool(len(b))


if __name__ == '__main__':
    a = "asad"
    b = "dasa"
    print(solution4(a, b))