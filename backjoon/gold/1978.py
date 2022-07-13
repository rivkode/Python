import sys

n = int(input())
lst = sys.stdin.readline().split()
lst_1 = []
lst = list(map(int, lst))
print(lst)

for x in lst:
    flag = True
    for i in range(2, x**0.5): # 루트를 사용해서 시간복잡도를 줄여본다 ! 유레카 !!!
        if x % i == 0:
            flag = False
    if flag:
        lst_1.append(x)


lst_1.remove(1)
print(len(lst_1))

