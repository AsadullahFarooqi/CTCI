
def brute_force_solution(a):
    #time complexity => O(n^2)
    for i in a:
        if a.count(i) > 1:
            return False

    return True


def solution(a):
    #time complexity => O(n)
    c = [0]*128
    for i in a:
        if c[ord(i)] >= 1:
            return False
        c[ord(i)] += 1
    return True


def solution2(a):
    #time complexity => O(n log n)
    a = sorted(a)
    for i in range(len(a)):
        if a[i] == a[i+1]:
            return False
    return True


if __name__ == '__main__':
    print(solution2("asad"))
