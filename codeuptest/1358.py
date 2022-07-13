# n = int(input())
# a = n//2
#
# for i in range(n+1):
#     if i % 2 == 1:
#         print(' ' * a + '*' * i)
#         a = a-1
#

n = int(input())

for i in range(1, n+1, 2):
    print(' ' * ((n-i)//2), end='')
    print('*'*i)