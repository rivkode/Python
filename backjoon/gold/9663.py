import sys

def promising(x): # 해당 col에서 i번째가 promising 한지를 판단
    for i in range(x):
        if abs(graph[x] - graph[i]) == x - i:
            return False
    return True

def n_queens(queen):
    global cnt # count 횟수를 세기 위해 전역변수 선언

    if queen == n: # n까지 깊게 내려갔다는 것은 모든 퀸이 모든 열에 나왔다는 것이므로  count를 해줌
        cnt += 1
        return

    for i in range(n): # 모든 j 를 돌며 대입
        # i 번째 열의 퀸을 놓지 않았다면
        if not visited[i]:
            graph[queen] = i # 배열 (queen, i)에 퀸을 둔다는 의미

            # 대각선의 겹치는 퀸 체크
            if promising(queen):
                # 백트래킹
                visited[i] = True # 퀸을 놓는다
                n_queens(queen + 1) # queen + 1을 해주어 이후 퀸을 놓을 수 있는 열을 찾는다
                visited[i] = False # 재귀 탐색 후 퀸을 n개 놓을 수 없다면 퀸을 놓지 않는 것으로 초기화 후 다른열을 탐색 - 시간복잡도를 줄여줌

### 왜이리 어렵지 ..

cnt = 0 # 퀸의 총 방법 수
n = int(sys.stdin.readline())
graph = [0 for _ in range(n)] # n번째 퀸의 위치
visited = [False for _ in range(n)] # 체스판 탐색 여부를 통해 시간복잡도를 크게 줄임

n_queens(0) # 함수 호출

print(cnt)