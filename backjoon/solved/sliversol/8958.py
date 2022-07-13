n = int(input())
cnt = 0
result = []


for i in range(n):
    result = input()

    for j in range(len(result)):
        if(result[j] == O):
            cnt += 1
            if(result[j+1] == O):
                cnt += 2
                if(result[j+3] == 0):
                    cnt += 3
