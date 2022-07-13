n = int(input())
a = []

for i in range(n):
    a = map(str, input().split())
    a = list(a)
    a.reverse()
    print("Case #{}: ".format(i+1), end='')
    print(*a)
