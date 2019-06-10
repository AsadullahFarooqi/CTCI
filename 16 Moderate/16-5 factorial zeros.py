def solution1():
    # brute force solution
    # find the factorial and then count the trailing zerose it it
    

    return ans

def optimal_solution(n):
    count = 0
    i = 5
    while n/i >= 1:
        count += int(n/i)
        i *= 5
    return count

  
if __name__ == '__main__':
    # solution1(n) 
    n = 1000
    print(optimal_solution(n)) 