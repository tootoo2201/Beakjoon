def solution(price, money, count):
    sum = 0
    for i in range(1,count+1):
        sum += price*i
    print(sum)
    if(money - sum > 0):
        return 0
    elif(money - sum <= 0):
        return sum - money
   