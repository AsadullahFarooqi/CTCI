def solution1(M):
    # this solution will make a copy of matrix and then change the elements of copied or answer matrix
    # which makes it space complexity to O(M) 
    ans = [[j for j in i] for i in M]
    for r in range(len(M)):
        for c in range(len(M[0])):
            if M[r][c] == 0:
                ans[r] = [0] * len(M[0])
                for i in range(len(M)):
                    ans[i][c] = 0
                
    return ans

if __name__ == '__main__':
    m = [
    [ 1,  2,  4,  55 ],
    [ 3,  0,  0,   6 ],
    [ 99, 1,  52,  7 ],
    ]

    print(solution1(m))
