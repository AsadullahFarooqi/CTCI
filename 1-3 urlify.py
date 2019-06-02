def solution(s):
    ans = ""
    for i in range(len(s.strip())):
        if s[i] == " ":
            ans += "%20"
            continue
        ans += s[i]


    print(ans)


if __name__ == '__main__':
    s = "Mr John Smith    "
    solution(s)