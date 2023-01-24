a = int(input())

for i in range(1, 1+a):
    print(" " * (a-i) + "*" * ((2*i)-1))
    if i == a:
        for j in range(1, 1+a):
            print(" " * (j) + "*"*((a*2) - (2*j)-1))