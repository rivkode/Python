n = int(input())

def sosu(x):
    if x == 1:
        result = 0
        return result
    for i in range(2, x):
        if x % i == 0:
            result = 0
            return result
    result = 1
    return result

total_num = 0
x_lst = list(map(int, input().split()))

for i in x_lst:
    total_num += sosu(i)

print(total_num)