from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
for i in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        q.append(cmd[1])
    elif cmd[0] == "pop":
        (print(q[0]), q.popleft()) if q else print(-1)
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":
        # if q:
        #     print(0)
        # else:
        #     print(1)
        print(0) if q else print(1)
    elif cmd[0] == "front":
        print(q[0]) if q else print(-1)
    elif cmd[0] == "back":
        print(q[-1]) if q else print(-1)