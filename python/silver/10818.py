import sys
input = sys.stdin.readline
n = int(input())
a = map(int, input().split())
a = list(a)

# for i in range(n):
#     a1 = int(input())
#     a.append(a1)

min_a = min(a)
max_a = max(a)

print(min_a, max_a)