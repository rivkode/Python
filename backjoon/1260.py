from collections import deque

#함수로 만들기
#전처리
#input, 과정, output 순으로 만들자


def dfs(N):
    visited[N] = True
    print(N, end="")
    for i in graph[N]:
        if not visited[i]:
            dfs(i)

# def bfs(N):
#     visited[N] = True
#     dq.append(N)
#     dq.popleft(i)
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
dq = deque()

for _ in range(M):
    graph.append(list(map(int, input().split()))) #해당 index에 값(근접한 노드)로 접근하여 재귀호출한다


visited = [False] * (N+1)
dfs(V)