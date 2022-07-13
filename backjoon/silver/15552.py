import sys

n = int(input())
input = sys.stdin.readline

for i in range(n):
    a, b = map(int, input().split())
    c = a+b
    print(c)
