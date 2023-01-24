n = int(input())

def hansu(n):
    cnt = 0
    if n < 100:
       cnt = n
       return cnt
    else:
        for i in range(100, n+1):
            num = str(i)
            a = int(num[0])
            b = int(num[1])
            c = int(num[2])

            if c-b == b-a:
                cnt += 1
        return cnt+99

print(hansu(n))
