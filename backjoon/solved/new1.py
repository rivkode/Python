import sys
from collections import deque
import time
input = sys.stdin.readline

Tc = int(input())
start_time = time.time()
for _ in range(Tc):
    err = False
    direction = True

    # input
    cmd = input().rstrip()
    n = int(input())
    dq = deque((input().rstrip()[1:-1]).split(','))

    # 예외 처리
    if len(dq) == 1 and dq[0] == '': #이건 빈배열이 주어졌을때 error만 출력하기위해 길이가 1인 이유는?
        dq.pop()

    for c in cmd:
        if c == "R":
            # direction이 False면 True, 아니면 False
            direction = True if not direction else False # R의 역할 오른쪽으로 뺄지, 왼쪽으로 뺄지
        else: #direction 이 False면 true, 아니면 direction 은 False
            if len(dq) == 0:
                err = True
                break
            # direction이 True면 popleft, 아니면 pop
            dq.popleft() if direction else dq.pop() #이건 삼항연산자다 ! 진짜 유용하고만

    # output
    if err:
        print("error")
    else:
        print("[", end='')
        while len(dq) > 1:
            print(dq.popleft() if direction else dq.pop(), end=',')
        if len(dq) == 1:
            print(dq.pop(), end='')
        print("]")
end_time = time.time()

print("time :", end_time - start_time)