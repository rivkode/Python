import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

num_lst = deque()

for i in range(1, n+1):
    num_lst.append(i)

try:
    while True:
        j = num_lst.popleft()
        print(j, end=" ")
        k = num_lst.popleft()
        num_lst.append(k)

        if len(num_lst) == 1:
            print(num_lst[0])
            break
except:
    if len(num_lst) == 1:
        print(num_lst[0])
