def replace(a,b):
    i = 0
    while i < len(a) and a[i] == b[i]:
        i += 1
    a[i] = b[i]
    print("replace: ", a[i])
    return a == b

def removal(a,b):
    i = 0
    while i < len(b) and a[i] == b[i]:
        i += 1
    print("remove: ", a[i])
    a.remove(a[i])
    return a == b

def insertion(a,b):
    i = 0
    while a[i] == b[i]:
        i += 1
    print("insert: ", b[i])
    a.insert(i, b[i])
    return a == b

def solution(a, b):
    a = list(a)
    b = list(b)
    if a == b:
        return True
    if len(a) == len(b):
        return replace(a,b)
    elif len(a)-1 == len(b):
        return removal(a,b)
    elif len(a)+1 == len(b):
        return insertion(a,b)

    return False
    

    

if __name__ == '__main__':
    a, b = "pales", "pale"
    a,b = "pale", "bale"
    print(solution(a, b))
