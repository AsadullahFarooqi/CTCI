def solution1(A, B):
    # brute force way compare every pair and compare the difference
    # time complexity O(A**B)
    min_diff = float("inf")
    a, b= 0,0
    for i in A:
        for j in B:
            if abs(i-j) < min_diff:
                min_diff = abs(i-j)
                a, b = i, j


    return a, b

def solution2(A, B):
    # optimal solution by sorting the lists
    # time complexity => O(A lg A + B lg B)
    A = sorted(A)
    B = sorted(B)
    a,b = 0, 0
    i, j = 0, 0
    min_diff = float("inf")
    while i < len(A) and j < len(B):
        if abs(A[i]-B[j]) < min_diff:
            min_diff = abs(A[i]-B[j])
            a, b = i, j

        if A[i] < B[i]: i += 1
        else: j += 1

    return A[a], B[b], min_diff

if __name__ == '__main__':
    A = [1, 3, 15, 11, 2]
    B = [23, 127, 235, 19, 8]
    print(solution2(A, B))
