a = int(input())
#
# for i in range(1, a+1):
#     print(" "*(i-1), end="")
#     for j in range(1, 1+a):
#         print("*"*(a*2 - ((j*2)-1)))
#

for i in range(1, a+1):
    print(" " * (i - 1) + "*"*(a*2 - ((i*2)-1)))