# dp = [0] * 1000
#
# n = int(input())
#
# def fibonacci(num):
#     global count0, count1
#
#     if num == 0:
#         count0 += 1
#         return dp[0]
#     elif num == 1:
#         dp[1] = 1
#         count1 += 1
#         return dp[1]
#     elif num > 1:
#         if dp[num] != 0:
#             return dp[num]
#         dp[num] = fibonacci(num-2) + fibonacci(num-1)
#         return dp[num]
#
#
#
# for _ in range(n):
#     count0 = 0
#     count1 = 0
#     num = int(input())
#     print("{} {}".format(count0, count1))

    # print(fibonacci(int(input())))



dp = [0] * 1000

n = int(input())
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])
