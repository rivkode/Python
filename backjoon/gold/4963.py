import sys
sys.setrecursionlimit(10**4) #재귀 깊이 제한
input = sys.stdin.readline

def dfs(x, y):

    if x < 0 or y < 0 or x >= h or y >= w: #index가 벗어나지 않도록 하기 위해
        return 0

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y + 1) # 모든 방향(아래,위, 대각선) 을 다 방문하며 돌기 위해 재귀함수
        dfs(x, y + 1)
        dfs(x + 1, y + 1)
        dfs(x + 1, y)
        dfs(x + 1, y - 1)
        dfs(x, y - 1)
        dfs(x - 1, y - 1)
        dfs(x - 1, y)

while True:
    w, h = list(map(int, input().split()))
    if w == 0 or h == 0: # 0이 input되면 break
        break
    else:
        result = 0 #result 0으로 초기값으로 세팅

        graph = []
        # for i in range(h):
        #     graph.append(list(map(int, input().split())))

        [graph.append(list(map(int, input().split()))) for i in range(h)]

        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    dfs(i, j)
                    result += 1
        print(result)
