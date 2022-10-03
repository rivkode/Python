a = int(input())
b = int(input())

def sosu(x):
    if x == 1:
        return
    for i in range(2, x):
        if x % i == 0:
            return
    return x

sosu_lst = []


for i in range(a, b+1):
    if sosu(i) != None:
        sosu_lst.append(sosu(i))

if len(sosu_lst) != 0:
    print(sum(sosu_lst))
    print(sosu_lst[0])
else:
    print(-1)