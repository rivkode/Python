a = input().split(" ")
b = int(input())
b_lst = []
# b_lst[0] = b // 60
# b_lst[1] = b % 60

if b >= 60:
    b_lst.append(b // 60)
    b_lst.append(b % 60)
    result_hour = int(a[0]) + b_lst[0]
    result_min = int(a[1]) + b_lst[1]

else:
    result_hour = int(a[0])
    result_min = int(a[1]) + b


print("{} {}".format(result_hour, result_min))
