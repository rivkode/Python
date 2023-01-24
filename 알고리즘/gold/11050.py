import sys
input = sys.stdin.readline

[n, k] = list(map(int, input().split()))

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result = result*i

    return result


answer = factorial(n)/(factorial(k)*factorial(n-k))
print(int(answer))