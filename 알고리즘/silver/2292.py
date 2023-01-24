import sys
input = sys.stdin.readline

n = int(input())

num = 1
cnt = 1
if n == 1:
    cnt = 1
else:
    cnt6 = 6
    while n > num:
        cnt += 1
        num += cnt6
        cnt6 += 6
print(cnt)



    # while True:
    #     if n <= 0:
    #         break
    #     else:
    #         n -= (6 * cnt)
    #         cnt += 1

# print(cnt)