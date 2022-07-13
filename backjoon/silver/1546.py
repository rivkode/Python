num = int(input())

# score = []
# a = input().split()
# score.append(a)
# print(score)
# score = list(map(int, score))
# print(score)
score = list(map(int, input().split()))

max_score = max(score)
M = max_score

score_result = []
for i in range(num):
    b = score[i]/M*100
    score_result.append(b)

sum_score = sum(score_result)
average = sum_score/len(score_result)
print(average)