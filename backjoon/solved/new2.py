import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

for _ in range(n):
    s = input() #R,D 명령어 입력받기
    num = int(input())
    dq = deque() #dq 덱 사용
    dq_lst = input()
    dq_lst = dq_lst[1:-2:1] #str 로 입력받으므로 [,]를 슬라이싱해준다
    dq_lst = dq_lst.split(",") #, 로 구분하여 숫자만 남기기 위해
    # print(dq_lst)

    if num != 0: #0 일때 error 나오게끔 하기 위해서
        for i in dq_lst: # dq 덱에 리스트형태로 숫자 넣기
            dq.append(int(i))

    lst = []
    # print(dq)
    flag1 = True # flag1 기준으로 R 뒤집기 효과 내기
    flag2 = True # flag2 기준으로 # error 시 빈배열 출력을 하지 않기 위해 error만 출력

    for i in range(len(s)):
        if flag1:
            if s[i] == "D":
                if len(dq) == 0:
                    print("error")
                    flag2 = False # error 시 빈배열 출력을 하지 않기 위해 error만 출력
                    break
                else:
                    dq.popleft()
            elif s[i] == "R":
                flag1 = False
        else:
            if s[i] == "D":
                if len(dq) == 0:
                    print("error")
                    flag2 = False  # error 시 빈배열 출력을 하지 않기 위해 error만 출력
                    break
                else:
                    dq.pop()
            elif s[i] == "R":
                flag1 = True

    if flag2: # error 시 빈배열 출력을 하지 않기 위해 error만 출력
        if flag1: #
            print("[", end="")
            for i in list(dq)[:-1]:
            #for i in lst:
                print(i, end=",")
            if len(dq) != 0:
                if list(dq)[-1] != 0: # 마지막 원소는 콤마를 같이 출력하지 않기 위해 -1까지만 출력하고 마지막은 숫자만
                    print(list(dq)[-1], end="")
                print("]")
            else:
                print("]") #dq의 길이가 0인 경우 []빈 배열을 출력
                break

            #print(list(dq))
        else:
            for i in range(len(dq)):
                tmp = dq.pop() # R일 경우 거꾸로 pop으로 빼주기 위해
                lst.append(tmp)
            print("[", end="")

            for i in lst[:-1]:
            #for i in lst:
                print(i, end=",")
            # if list(dq)[-1] != 0:
            if len(lst) != 0:
                print(lst[-1],end="")
            print("]")