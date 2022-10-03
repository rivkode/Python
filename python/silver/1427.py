s = input()
n_lst = []
for i in s:
    n_lst.append(int(i))
n_lst.sort(reverse=True)
print(*n_lst, sep="")