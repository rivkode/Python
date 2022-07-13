x, y, w, h = map(int, input().split())

if (w/2 < x and h/2 < y):
    if (w-x) < (h-y):
        print(w-x)
    elif (w-x) > (h-y):
        print(h-y)
    elif (w-x) == (h-y):
        print(w-x)
else:
    if (x < y):
        print(x)
    elif (x > y):
        print(y)
    elif (x == y):
        print(x)

    elif (w/2 == x and h/2 == y):
        print(x)