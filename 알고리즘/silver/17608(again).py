# import sys
# input = sys.stdin.readline
#
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# set_lst = set(lst)
# a = lst[-1]
# cnt = 0
#
# for j in set_lst:
#     if j > a:
#         cnt += 1
# print(cnt+1)

import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
max_height = lst[-1]
cnt = 1

for i in range(n):
    if max_height < lst[n-i-1]:
        cnt +=1
        max_height = lst[n-i-1]
print(cnt)