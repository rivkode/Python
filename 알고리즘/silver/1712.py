a, b, c = map(int, input().split())

def break_even_point(a, b, c):
    point = 0

    if b >= c:
        point = -1
    else:
        point = (a/(c-b))+1

    return int(point)

print(break_even_point(a, b, c))