a = int(input())
b = int(input())
c = int(input())

num = a*b*c
strnum = list(map(int, str(num)))

cnt0 = cnt1 = cnt2 = cnt3 = cnt4 = cnt5 = cnt6 = cnt7 = cnt8 = cnt9 = 0

for i in range(8):
    if strnum[i] == 0:
        cnt0 += 1
    if strnum[i] == 1:
        cnt1 += 1
    if strnum[i] == 2:
        cnt2 += 1
    if strnum[i] == 3:
        cnt3 += 1
    if strnum[i] == 4:
        cnt4 += 1
    if strnum[i] == 5:
        cnt5 += 1
    if strnum[i] == 6:
        cnt6 += 1
    if strnum[i] == 7:
        cnt7 += 1
    if strnum[i] == 8:
        cnt8 += 1
    if strnum[i] == 9:
        cnt9 += 1

print(cnt0)
print(cnt1)
print(cnt2)
print(cnt3)
print(cnt4)
print(cnt5)
print(cnt6)
print(cnt7)
print(cnt8)
print(cnt9)

