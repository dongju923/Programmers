def solution(x, n):
    if x == 0:
        return [0]*n
    elif x > 0:
        return [i for i in range(x, n*x+1, x)]
    elif x < 0:
        return [i for i in range(x, n*x-1, x)]
    
