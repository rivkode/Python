import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    num = int(input())
    lst.sort()
    if num != 0:
        lst.append(int(input()))
    elif num == 0:
        if not lst:
            print(0)
        else:
            print(lst[-1])