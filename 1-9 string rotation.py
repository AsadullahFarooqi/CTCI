def solution(s1,s2):
    # this statement checks if the length of the strings isn't
    # equal then s2 can't rotation of s1
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        # this loop will keep rotating the s1 and will check 
        # if it is equal to s2
        
        # s1 will be replaced by it's rotation. 
        s1 = s1[1:]+s1[0]
        if s1 == s2:
            # if 
            return True
        
    return False

if __name__ == "__main__":
    s1,s2 = "waterbottle","erbottlewat"
    print(solution(s1,s2))
