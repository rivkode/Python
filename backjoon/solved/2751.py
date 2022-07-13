import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    s = int(input())
    lst.append(s)
lst.sort()

for i in range(n):
    print(lst[i])