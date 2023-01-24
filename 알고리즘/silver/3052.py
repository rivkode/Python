# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# num5 = int(input())
# num6 = int(input())
# num7 = int(input())
# num8 = int(input())
# num9 = int(input())
# num10 = int(input())

cnt = 0
a = 0
num = []

for i in range(10):
    a = int(input())
    num.append(a)



b1 = num[0] % 42
b2 = num[1] % 42
b3 = num[2] % 42
b4 = num[3] % 42
b5 = num[4] % 42
b6 = num[5] % 42
b7 = num[6] % 42
b8 = num[7] % 42
b9 = num[8] % 42
b10 = num[9] % 42

b = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]


b = set(b)
blen = len(b)


print(blen)