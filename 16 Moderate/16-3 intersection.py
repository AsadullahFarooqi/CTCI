def solution1(l1, l2):
     s1 = slope(l1)
     s2 = slope(l2)
     y_intercept1 = y_intercept(l1[0],s1)
     y_intercept2 = y_intercept(l2[0],s2)
     if s1 == s2 and y_intercept1 == y_intercept2:
     	return "they are the same lines"
     	

def slope(x1,y1, x2,y2):
	return (y2-y1)/(x2-x1)

def y_intercept(x,y, slope):
	return y-(x*slope)

if __name__ == '__main__':
    line1 = ()
    line2 = ()
    solution(line1, line2)