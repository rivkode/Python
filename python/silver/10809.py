import sys
input = sys.stdin.readline

s = list(input().rstrip())

result_list = []
for _ in range(26):
    result_list.append(-1)

for i, apb in enumerate(s):
    insert_num = ord(apb)-97
    if result_list[insert_num] == -1:
        result_list[insert_num] = i

print(*result_list)