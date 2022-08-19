## youtube 강의를 통해 개념이해를 위한 코드풀이 과정

def n_queens(col, i):
    n = len(col) - 1 # col의 길이를 n+1 을 해주었기 때문
    global cnt # count 횟수를 세기 위해 전역변수 선언
    if (promising(col, i)): # promising 판단 False일 경우 실행되지 않음 = 다른 퀸에게 잡힘
        if (i == n): # n까지 깊게 내려갔다는 것은 모든 퀸이 모든 열에 나왔다는 것이므로  count를 해줌
            # print(col[1: n+1])
            cnt += 1
        else: # 그게 아니라면
            # 여기서 부터 핵심 10 ~ 13까지
            for j in range(1, n+1): # 모든 j 를 돌며 대입
                col[i+1] = j # 1차원 배열로 퀸 표현, +1 인 이유는 i 가 0부터 시작하기 때문
                # 즉 n=4 일 경우 col[i + 1] = 1, 2, 3, 4 으로 각 col 열을에 대해 퀸을 위치시키면서 promising한지 판별
                n_queens(col, i+1) # i를 1 증가시키며 재귀로 호출 +1 시키는 이유는 다음 행으로 가기 위함임

def promising(col, i): # 해당 col에서 i번째가 promising 한지를 판단
    k = 1
    flag = True
    while (k < i and flag): # i 가 될때까지 계속 반복
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)): # 열이 같은지 확인
            # 1차원 배열로 퀸을 저장하여, 절댓값을 통해 열에서의 차이와 행에서의 차이의 절대값은 같음을 이용하여 대각선체크를 해준다
            flag = False # 만약 하나라도 일치한다면 퀸에게 잡히므로 False로 판정
        k += 1
    return flag # flag 반환, promising 판별
### 왜이리 어렵지 ..

cnt = 0
n = int(input()) # 숫자 인풋
col = [0] * (n+1) # n+1인 이유는 인덱스 0번째 인덱스는 제외하기 위함

n_queens(col, 0) # 함수 호출을 함, 파라미터로 col

print(cnt)