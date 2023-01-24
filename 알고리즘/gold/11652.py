import sys
t1 = sys.maxsize


n = int(input()) #숫자 개수 입력받기
n_lst = [] #숫자들의 리스트
for i in range(n):
    n_lst.append(input())

n_lst.sort() #숫자 정렬
new_lst = list(set(n_lst)) #숫자의 중복 제거
count_lst = [] #숫자의 개수

for i in range(n): #숫자의 count 개수 세기
    count_lst.append(n_lst.count(new_lst[i]))

dic = {}
for i in range(len(new_lst)):
    dic[new_lst[i]] = count_lst[i]

i = max(count_lst) # count_lst = 중복의 갯수의 모음, 그것중 최대 중복의 갯수
# num = count_lst.index(i) # count_lst 의 최대중복의 인덱스

max_lst = []
if count_lst.count(i) == 1: # count_lst 의 중복많은수가 1 이라면 중복수는 하나
    max_num = new_lst[count_lst.index(i)] # new_lst의 최대 수
    print(max_num)
else:
    for j in range(count_lst.count(i)):
        max_lst.append(dic[i]) #최대 개수의 수를 추가
    
    max_lst.sort()
    print(max_lst[0])

