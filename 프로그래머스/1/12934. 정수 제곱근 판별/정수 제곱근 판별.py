def solution(n):
    a = n**(1/2)
    if(n%a == 0):
        return (a+1)**2
    else:
        return -1