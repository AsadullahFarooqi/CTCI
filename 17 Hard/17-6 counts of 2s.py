def solution(n):
    ans = 0
    for i in range(n+1):
        ans += str(i).count("2")
    print(ans)
    return ans


if __name__ == '__main__':
    solution(25)