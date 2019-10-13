def solution1(M):
    # it's a simple brute force solution where we copy each 
    # colum and add it to the new matrix as a row. In Mathematics
    # it would be transparent of matrix.

    ans = []
    for row in range(len(M[0])):
        row_ = [M[col][row] for col in range(len(M))]
        row_.reverse()
        ans.append(row_)

    return ans


def solution2(M):
    # it's in-place algorithm
    # fist we will reverse the rows of the matrix because it solves the 
    # diagonal cells so we don't need to worry about that.
    # this step takes O(len(M))

    M.reverse()
    for row in range(len(M)):
        for col in range(row):
            M[row][col], M[col][row] = M[col][row], M[row][col]

    return M

def rotateImage(a):
    print(a[::-1])
    return zip(*a[::-1])

if __name__ == '__main__':
    m = [
    [1,  2,  3],
    [5,  6,  7],
    [9, 10, 12]
    ]

    m = [
        [0,  1,  2,  3,  4,  5,   6,  7],
        [8,  9,  10, 11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20, 21, 22, 23],
        [24, 25, 26, 27, 28, 29, 30, 31],
        [32, 33, 34, 35, 36, 37, 38, 39],
        [40, 41, 42, 43, 44, 45, 46, 47],
        [48, 49, 50, 51, 52, 53, 54, 55],
        [56, 57, 58, 59, 60, 61, 62, 63]]

    # [56, 57, 58, 59, 60, 61, 62, 63]
    # [48, 49, 50, 51, 52, 53, 54, 55]
    # [40, 41, 42, 43, 44, 45, 46, 47]
    # [32, 33, 34, 35, 36, 37, 38, 39]
    # [24, 25, 26, 27, 28, 29, 30, 31]
    # [16, 17, 18, 19, 20, 21, 22, 23]
    # [8,   9, 10, 11, 12, 13, 14, 15]
    # [0,   1,  2,  3,  4,  5,  6,  7]

    
    for r in solution2(m):
        print(r)