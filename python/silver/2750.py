n = int(input())
num_lst = []
for _ in range(n):
    num_lst.append(int(input()))

num_lst = sorted(set(num_lst))

for i in num_lst:
    print(i)