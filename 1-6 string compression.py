def string_compression(s):
    ans = ""
    temp = 0  # temporary variable that holds the number of times the character appears
    # the loop will iterate throw the charachters till the 2nd last one
    for i in range(len(s) - 1):
        # this if checks if the current charachter is equal to the next one
        if s[i] == s[i + 1]:
            # if yes add one to temp and continue
            temp += 1
            continue
    
        # when current charachter is not equal to the next then it'll merge it with ans and the temp count
        ans += s[i] + str(temp + 1)
        temp = 1
    # this line handles the last charachter since the temp has already stored the count of last character
    ans += s[-1] + str(temp)
    return ans


if __name__ == "__main__":
    n = "aabcccccaaad"
    print(string_compression(n))
