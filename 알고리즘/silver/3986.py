import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
    a = input().rstrip()
    stack = []

    for i in range(len(a)):
        if stack:
            if a[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(a[i])
        else:
            stack.append(a[i])

    if not stack:
        cnt += 1
print(cnt)