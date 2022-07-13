import sys
import time
from collections import deque
input = sys.stdin.readline
start_time = time.time()


n = list(map(int, input().split()))
dp = deque() #deque([]) 로 해야할까 ? 차이점은 ...
new_lst = []
cnt = 0

for i in range(1, n[0]+1):
    dp.append(i)
# print(dp)

for i in range(n[0]):

    for _ in range(n[1]-1):
        tmp = dp.popleft()
        dp.append(tmp)
    new_lst.append(dp[0])
    dp.popleft()

# print(new_lst)
print("<", end="")
for i in new_lst:
    if i == new_lst[-1]:
        print(i, end=">")
        break
    print(i, end=", ")
end_time = time.time()
print()
print("time :", end_time - start_time)


# if cnt == n[0]:
#     break
#if len(new_lst) == 7: # 매번 new_lst 를 돌아야 하므로 시간복잡도가 좋지 않음 cnt를 활용하자
    #break


