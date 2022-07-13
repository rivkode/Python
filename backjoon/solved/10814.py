import sys


n = int(sys.stdin.readline())
# people_lst = {}
people_lst = []
for i in range(n):
    people_lst.append(list(sys.stdin.readline().split()))

people_lst.sort(key = lambda x:int(x[0]))

for s in range(n):
    print(people_lst[s][0], people_lst[s][1])


# print(people_lst)
#     people_lst[s[0]] = s[1]
#
# people_lst = sorted(people_lst.items())
# print(people_lst)
#
# for key, value in people_lst:
#     print(key, value)