import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())


# while c < v:
#     c += a
#     cnt += 1
#     if c >= v:
#         break
#     c -= b

cnt = (v-b)/(a-b)


print(int(cnt) if cnt == int(cnt) else int(cnt)+1)

