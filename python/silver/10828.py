import sys
input = sys.stdin.readline

n = int(input())
stack = []


for i in range(n):
    x = input().split()


    if x[0] == "push":
        stack.append(x[1])
    elif x[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif x[0] == "size":
        print(len(stack))
    elif x[0] == "empty":
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    elif x[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])

