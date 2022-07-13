a = int(input())

for i in range(1, a+1):
    print(" "*(i-1) + "*"*((a*2) - ((i*2)-1)))
    if i == a:
        for j in range(2, 1+a):
            print(" "*(a-j) + "*"*((2*j)-1))