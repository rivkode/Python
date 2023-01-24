n = int(input())

n_lst = list(map(int, input().split()))

new_lst = sorted(list(set(n_lst)))

idx_lst = []
for i in n_lst:
    idx_lst.append(new_lst.index(i))
print(*idx_lst)