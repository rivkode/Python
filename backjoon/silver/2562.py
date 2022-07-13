#
# a = []
# cnt = 0
# while cnt < 9:
#     cnt += 1
#     a = map(int, input().split('\n'))
#     max_a = max(a)
#     a.append(a[cnt])
#
#
# print(a)
# for i in range(9):
#     if max_a == a[i]:
#         print(max(a))
#         print(i+1)
#

num_list = []

for i in range(9):
    num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list))+1)