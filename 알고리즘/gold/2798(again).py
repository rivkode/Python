# import random
# [n, m] = list(map(int, input().split()))
# lst = list(map(int, input().split()))
# lst = lst.sort()
# num_lst = []
#
# rnum = random.randint(1, n)
#
# for i in range(3):
#     while rnum in num_lst:
#         rnum = random.randint(1, n)
#     num_lst.append(rnum)
#
# lst[num_lst[0]] + lst[num_lst[1]] + lst[num_lst[2]]

[n, m] = list(map(int, input().split()))
lst = list(map(int, input().split()))
result = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if lst[i] + lst[j] + lst[k] > m:
                continue
            else:
                result.append(lst[i] + lst[j] + lst[k])

result = max(result)
print(result)

