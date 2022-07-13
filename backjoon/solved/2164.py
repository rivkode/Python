import sys
from collections import deque

n = int(sys.stdin.read())
num_lst = deque([])

for i in range(1, n+1):
    num_lst.append(i)

while True:
    if len(num_lst) == 1:
        print(num_lst[0])
        break
    else:
        num_lst.popleft()
        tmp = num_lst.popleft()
        num_lst.append(tmp)