

while True:
    num = list(map(int, input()))

    if num[0] == 0:
        break

    a = len(num) - 1
    result = 0

    for i in range(a+1):
        if num[i] != num[a-i]:
            result = "no"
            break
        # elif num[a-1] != num[i+1]:
        #     result = "no"
        else:
            result = "yes"
    print(result)
