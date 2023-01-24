import sys
input = sys.stdin.readline

n = int(input())

def make1(n):
    share3 = n // 3 #3으로 나눈 몫, count 에 추가
    remainder3 = n % 3 #3으로 나눈 나머지, 2로 다시 나눔
    if remainder3 == 2:
        result = share3 + 1
        return result
    elif remainder3 == 1:
        result = share3
        return result
    elif remainder3 == 0:
        result = share3 - 1
        return result

print(make1(n))