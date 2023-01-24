a = int(input())
b = list(map(int, input()))

num = 0
for i in range(len(b)):
    num = num + b[i]

print(num)