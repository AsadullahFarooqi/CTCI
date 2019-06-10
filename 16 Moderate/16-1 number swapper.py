def solution1(x,y):
    # using python technique
    return y, x

def solution2(x,y):
    # using math technique
    
    x = x-y
    y = y+x
    x = y-x

    return x,y

def solution3(x,y):
    # using bitmanupilation
    # xor ^ operation
    # a = 10001
    # b = 00111
    # a = 10110 => a^b
    # b = 10001 => a^b 
    # a = 00111 => a^b
    pass

if __name__ == '__main__':
    x, y = 5, 6
    print(solution1(x,y))
    print(solution2(x,y))