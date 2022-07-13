import sys
input = sys.stdin.readline

n = int(input())

lst = []

for i in range(n):
    [a, b] = map(int, input().split())
    lst.append([a, b])


lst.sort()
# lst_int = list(map(int, lst))

for i in lst:
    print("{} {}".format(i[0], i[1]))
    # print(type(i[0]))