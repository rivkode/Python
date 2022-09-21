from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_lst = list(map(int, input().split()))

dq = deque()
count = 0

for i in range(1, int(n)+1):
    dq.append(int(i))

for j in num_lst:
    centerIndex = len(dq) // 2

    if dq.index(j) <= centerIndex:

        while True: #while 사용을 다시 생각해보자 !! for 문을 무작정 사용하려 하는 것은 금지 !!
            if j == dq[0]:
                dq.popleft()
                break
            else:
                tmp = dq.popleft()
                dq.append(tmp)
                count += 1

    elif dq.index(j) > centerIndex:

        while True:
            if j == dq[0]:
                dq.popleft()
                break
            else:
                tmp = dq.pop()
                dq.appendleft(tmp)
                count += 1

print(count)