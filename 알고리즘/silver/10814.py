import sys
input = sys.stdin.readline

n = int(input())

people_lst = []
for i in range(n):
    a, b = map(str, input().split())
    people_lst.append([int(a), b])

# print(people_lst)
d2 = sorted(people_lst, key=lambda x: x[0])

for key, value in d2:
    print(key, value)