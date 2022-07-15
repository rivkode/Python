from collections import deque
import sys
input = sys.stdin.readline
num = int(input())

for i in range(num):
    dq = deque(input())
    sum = 0
    cnt = 0
    for j in range(len(dq)):
        v = dq.popleft()
        if v == "O":
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)