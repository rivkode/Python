import sys
input = sys.stdin.readline
import time

start_time = time.time()

n, m, k = input().split()
num_lst = list(map(int, input().split()))
result = 0
max_num = max(num_lst)
new_lst = []

if num_lst.count(max_num) > 1:
    result = max_num * int(m)
else:
    for i in num_lst:
        if i == max_num:
            num_lst.remove(max_num)
    second_num = int(max(num_lst))
    share = int(m) // (int(k)+1)
    remainder = int(m) % (int(k)+1)
    result = ((int(k)) * max_num * share) + (remainder * max_num) + (share * second_num)
end_time = time.time()
print(result)

print("time :", end_time - start_time)