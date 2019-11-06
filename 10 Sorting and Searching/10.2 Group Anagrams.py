def sol(a):
    d = {sorted(i): [] for i in a}

    for s in a:
        d[sorted(s)].append(s)

    ans = []
    for v in d.values():
        ans += v
    return ans