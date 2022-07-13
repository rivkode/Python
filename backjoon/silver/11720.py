a = int(input())
b = map(int, input())
b = list(b)

c = 0
for i in range(len(b)):
    c = c + b[i]

print(c)