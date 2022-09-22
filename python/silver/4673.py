def d(num):
    str_num = str(num)
    num_len = len(str_num)
    num_sum = 0
    for i in range(num_len):
        num_sum += int(str_num[i])
    result = num + num_sum
    return result

num_list = list(range(1,10001))
d_list = []

for i in range(1, 10001):
    d_list.append(d(i))


result = list(set(num_list) - set(d_list))
result.sort()

for i in result:
    print(i)