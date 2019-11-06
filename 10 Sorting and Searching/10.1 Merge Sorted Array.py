def sol(a, b):
    
    for i in range(len(a)):
        j = i
        while j < len(b) and b[j] <= a[i]:
            a = a[:i] + a[i+1:]
        if i < len(b):

