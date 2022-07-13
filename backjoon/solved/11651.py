import sys
input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    [a, b] = map(int, input().split())
    lst.append([b, a])

lst.sort()

for i in range(n):
    print("{} {}".format(lst[i][1], lst[i][0]))
    # print(type(lst[i][0]))
