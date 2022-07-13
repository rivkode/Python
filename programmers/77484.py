def solution(lottos, win_nums):
    answer = []
    new_lot = []
    cnt1 = 0
    cnt2 = 0

    for i in lottos:
        if i == 0:
            cnt1 += 1
            continue
        else:
            new_lot.append(i)

    if lottos.count(0) == 6:
        cnt1 -= 1

    for i in new_lot:
        for j in win_nums:
            if i == j:
                cnt2 += 1
            else:
                continue
    if cnt2 == 0:
        cnt2 = 1

    answer = [7 - (cnt1 + cnt2), 7 - cnt2]

    return answer