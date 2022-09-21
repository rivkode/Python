import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    lst = list(input())
    score = 0
    sum_score = 0
    for ox in lst:
        if ox == "O":
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)