from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque()

def empty():
    if len(dq) == 0:
        return 1
    else:
        return 0
def size():
    return len(dq)
num = 10

for i in range(n):
    s = input().split()
    print(s, num)
    if s == "push_front":
        dq.appendleft(num)
    elif s[0] == "push back":
        dq.append(s[1])
    elif s[0] == "pop_front":
        if not dq:
            print(-1)
        else:
            tmp = dq.popleft()
            print(tmp)
    elif s[0] == "pop_back":
        if not dq:
            print(-1)
        else:
            tmp = dq.pop()
            print(tmp)
    elif s[0] == "size":
        print(size())
    elif s[0] == "empty":
        print(empty())
    elif s[0]== "front":
        if empty() == 1:
            print(-1)
        else:
            print(dq[0])
    elif s[0] == "back":
        if empty() == 1:
            print(-1)
        else:
            print(dq[-1])
