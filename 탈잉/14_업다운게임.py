import random

ans = random.randint(1, 100) #ans는 answer의 줄임말임
print("--- 업다운게임을 시작합니다 ---")
cnt = 0

while True:
    num = int(input("숫자를 입력하세요>>"))
    cnt += 1
    if ans == num:
        print("정답입니다")
        break
    elif ans > num:
        print("Up")
    elif ans < num:
        print("Down")
print("{}회 만에 정답을 맞추셨습니다".format(cnt))