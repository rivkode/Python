arr = [3,2,4,4,2,5,2,5,5]

result = []
new_lst = []

for i in arr:
    if i not in new_lst:
        new_lst.append(i) #new_lst는 3245 임 - 순서를 위해set사용을 안함
print(new_lst)

for i in range(len(new_lst)): #길이는 4
    if arr.count(new_lst[i]) > 1: #중복일때만
        result.append(arr.count(new_lst[i])) #숫자개수 result에 추가
        for j in arr: #숫자를 arr에서 없앰
            #arr.remove(new_lst[i]) # 인덱스 위치 들어가야함
            if j == new_lst[i]:
                arr.pop(j)
    else:
        arr.pop(0)
        new_lst.pop(0)

print(result)