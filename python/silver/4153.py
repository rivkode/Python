def tri(x, y, z):
    if x ** 2 + y ** 2 == z ** 2:
        result = "right"
        return result
    else:
        result = "wrong"
        return result



while True:
    x, y, z = map(int, input().split())
    d =[]
    d += [x, y, z]
    if x ==0 and y == 0 and z == 0:
        break

    c = max(d)
    d.remove(max(d))
    a = d[0]
    b = d[1]

    print(tri(a, b, c))

