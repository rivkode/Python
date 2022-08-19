import sys
input = sys.stdin.readline

case = int(input())

def func():
    n = list(map(int, input().split(' ')))
    a_lst = list(map(int, input().split(' ')))
    a_lst.sort()
    b_lst = list(map(int, input().split(' ')))
    b_lst.sort()
    cnt = 0
    for i in a_lst:
        for j in b_lst:
            if i > j:
                cnt += 1
            else:
                break
    return print(cnt)


for _ in range(case):
    func()
