def solution1(M, rotate=None):
    # it's a simple brute force solution where we copy each colum and add it to the new matrix
    # and we keep doing that till we have done all columns

    args = (0, len(M[0]), 1)

    if rotate == "A" or rotate == "a":
        args = (len(M[0])-1, -1, -1)

    ans = []
    for col in range(*args):
        temp = [M[row][col] for row in range(len(M)-1,-1,-1)]
        ans.append(temp)
    return ans

if __name__ == '__main__':
    m = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ]

    print(solution1(m, "a"))