import sys
input = sys.stdin.readline

n = int(input())
queue = []
a = 0

for i in range(n):
    s = input().split()

    if s[0] == "push":
        queue.append(int(s[1]))

    elif s[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)
    elif s[0] == "size":
        print(len(queue))
    elif s[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif s[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif s[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
