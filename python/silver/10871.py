import random

n, x = map(int, input().split())
d = map(int, input().split())
d = list(d)

c = []
cnt = 0

for i in range(n):
    if x > d[i]:
        c.append(d[i])
        cnt += 1

for i in range(cnt):
    print(c[i],end=' ')
