import sys
input = sys.stdin.readline

s = input().rstrip()
s = s.upper()

num_list = []
for _ in range(26):
    num_list.append(0)

for i in s:
    num_list[ord(i)-65] += 1

max_num_index = num_list.index(max(num_list))
cnt = 0
for i in range(26):
    if num_list[i] == max(num_list):
        cnt += 1
if cnt == 1:
    print(chr(max_num_index+65))
else:
    print("?")