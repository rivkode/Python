a = int(input())

for i in range(1, a+1):
    print("*"*i + " " * 2*(a-i)+"*"*i)
    if i == a:
        for j in range(1, a+1):
            print("*" * ((a) - j) + " "*2*j + "*" * ((a) - j))

