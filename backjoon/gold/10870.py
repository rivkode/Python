import sys
from collections import deque
input = sys.stdin.readline
dq = deque()

n = int(input())
num = deque([0, 1]) #pop하기 위해 덱 사용

for i in range(n-1): #재귀시 for문 돌때 저장하려고
    c = num[i] + num[i+1]
    num.append(c)

a = num.pop()

if n == 0: #0 예외처리 함
    print(0)
else:
    print(a)
