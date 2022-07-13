r, g, b = map(int, input().split())

# 오름차순으로 0-1-2-3-4-5-6-7


for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print("{} {} {}".format(i, j, k))
print(r*g*b)

