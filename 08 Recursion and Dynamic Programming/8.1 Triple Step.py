def bf_sol(n):
    if n < 0: return 0
    elif n == 0: return 1
    return bf_sol(n-1) + bf_sol(n-2) # + bf_sol(n-3)


if __name__ == '__main__':
    n = 5
    print(bf_sol(n))
