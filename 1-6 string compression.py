def string_compression(s):
    ans = ""
    temp = 0
    for i in range(len(s)-1):
        if s[i]  == s[i+1]:
            temp += 1
            continue
        ans += s[i]+str(temp+1)
        temp = 1
    ans += s[-1] + str(temp)
    return ans

if __name__ == "__main__":
    n = "aabcccccaaa"
    print(string_compression(n))
