def solution(numbers, hand):
    answer = ''
    left_position = 0
    right_position = 0

    #     if hand == "left":
    #         hand = "L"
    #     else:
    #         hand = "R"

    # number_lst = [[1,2,3], [4,5,6], [7,8,9], ["*",0,"#"]]

    lst = []

    for i in range(len(numbers)):

        left_count = 0
        right_count = 0

        if numbers[i] == 1 or 4 or 7:
            lst.append("L")
            left_position = numbers[i]

        elif numbers[i] == 3 or 6 or 9:
            lst.append("R")
            right_position = numbers[i]

        elif numbers[i] == 2 or 5 or 8 or 0:
            lst.append("R")

            # if left_count == right_count:
            #     lst.append(hand)
            # elif left_count < right_count:
            #     lst.append("L")
            # elif left_count > right_count:
            #     lst.append("R")

            # 가까운 순서

    answer = "".join(lst)

    return answer

