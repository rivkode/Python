arr = [1,2,2,3,3,3]
for j in arr:  # 숫자를 arr에서 없앰
    # arr.remove(new_lst[i]) # 인덱스 위치 들어가야함
    if j == 3:
        arr.pop(j)
# arr.remove(3)
print(arr)