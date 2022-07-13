def solution(answer):
    answer = []
    a = [1,2,3,4,5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a1, b1, c1 = 0, 0, 0
    cnt = [0, 0, 0]


    for i in range(len(answer)):
        if a[i%5] == answer[i]:
            cnt[0] += 1
        if b[i%8] == answer[i]:
            cnt[1] += 1
        if c[i%10] == answer[i]:
            cnt[2] += 1

    max_cnt = max(cnt)

    for i in range(3):
        if cnt[i] == max_cnt:
            answer.append(i+1)

    return answer