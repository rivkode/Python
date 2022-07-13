def solution(array, commands):

    while True:
        for i in range(len(commands)):

            a = commands[i][0]
            b = commands[i][1]
            c = commands[i][2]
            d = array
            d = s[a:b]

            d.sort()

            answer = d[c]
            return answer

            if i == 0:
                break
