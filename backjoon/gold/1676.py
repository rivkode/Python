# from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
num = 1

for i in range(1, n+1):
    num = num * i
    if i == n:
        # print(num)
        break

num = list(str(num))
cnt = 0

for i in num:
    v = num.pop()
    if v == "0":
        cnt += 1
    else:
        break
print(cnt)
