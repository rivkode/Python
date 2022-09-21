import sys
input = sys.stdin.readline

n = int(input())
stack = []
# s = []

for i in range(n):
    # s = list(map(int, input()))
    s = int(input())

    if s == 0:
        stack.pop()
    else:
        stack.append(s)
sum_s = sum(stack)

print(sum_s)