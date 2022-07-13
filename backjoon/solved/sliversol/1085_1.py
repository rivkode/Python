x, y, w, h = map(int, input().split())
min1 = 999

print(min(x, y, w-x, h-y))

if w/2 < x:
    if h/2 < y:
        if w-x < h-y:
            min1 = w-x
        else:
            min1 = h-y
    else:
        if w-x < y:
            min1 = w-x
        else:
            min1 = y
else:
    if h/2 < y:
        if x < h-y:
            min1 = x
        else:
            min1 = h-y
    else:
        if x < y:
            min1 = x
        else:
            min1 = y
print(min1)
