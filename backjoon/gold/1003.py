# import sys
# input = sys.stdin.readline
#
# n = int(input())
# dp = [0] * 1000
#
# def fibonacci(num):
#     global count0, count1
#
#     if num == 0:
#         count0 += 1
#         return dp[0]
#     elif num == 1:
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
# for i in range(n):
#     count0 = 0
#     count1 = 0
#     num = int(input())
#     fibonacci(num)
#     print("{} {}".format(count0, count1))




n = int(input())
global num

def func1(num0): #0의 개수
    dp = [0] * 1000
    dp[0] = 1
    for i in range(2, num0 + 1):
        dp[i] = dp[i - 2] + dp[i - 1]  # 0의 개수,
    result = dp[num0]

    return result

def func2(num1): # 1의 개수
    dp = [0] * 1000
    dp[1] = 1
    for i in range(2, num1 + 1):
        dp[i] = dp[i - 2] + dp[i - 1]  # 0의 개수,
    result = dp[num1]
    return result

for i in range(n):
    num = int(input())

    count0 = func1(num)
    count1 = func2(num)

    print("{} {}".format(count0, count1))

