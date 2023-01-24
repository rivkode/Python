import sys
input = sys.stdin.readline

text_num = int(input())

for i in range(text_num):
    score = list(map(int, input().split()))
    score_num = score[0]
    score_sum = 0
    cnt = 0

    for j in range(1, score_num+1):
        score_sum += score[j]

    score_ave = score_sum/score_num

    for i in score[1:]:
        if i > score_ave:
            cnt += 1

    score_rate = (cnt/score_num)*100

    print(f'{score_rate:.3f}%')