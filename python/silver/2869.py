import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

cnt = (v-b)/(a-b) # 총 걸리는 날짜

if cnt != int(cnt):  # 만약 소수점이 나오면 +1일을 해준다
    cnt += 1

print(int(cnt))