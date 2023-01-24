# n = int(input())
# n_lst = list(input())
# m = int(input())
# m_lst = list(input())
# result_lst = []
#
# for i in range(m):
#     for j in range(n):
#         if m_lst[i] != n_lst[j]:
#             if j == m-1:
#                 result_lst.append(0)
#             else:
#                 continue
#
#         else:
#             result_lst.append(1)
#             break
#
#
# print(result_lst)
#

from sys import stdin, stdout
n = stdin.readline()
N = set(stdin.readline().split())
m = stdin.readline()
M = stdin.readline().split()

for i in M:
    stdout.write('1\n') if i in N else stdout.write('0\n')
