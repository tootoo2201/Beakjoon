x,y,w,h = map(int, input().split())
if(h-y > y):
    y_min = y
else:
    y_min = h-y
if(w-x > x):
    x_min = x
else:
    x_min = w-x
if(y_min > x_min):
    result = x_min
    print(result)
else:
    result = y_min
    print(result)