from collections import deque
import sys
input = sys.stdin.readline #문자열 단위로 빠르게 읽어들이기 위해 작성

def bfs(graph, x, visited): #bfs 가 더 빠르므로 bfs를 만들어 보았다
    queue = deque([x])
    visited[x] = True

    while queue:
        v = queue.popleft()
        for j in graph[v]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True

n, m = list(map(int, input().split()))
graph = []
for i in range(n+1): #graph 를 이차원 배열로 만들기 위해 for문을 사용하였다
    graph.append([])

visited = [False] * (n+1)
for i in range(m):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)
    # graph[u].sort() #방향이므로 sort()를 해주지 않아도 된다
    # graph[v].sort()

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1 #위 bfs 를 한번 빠져나오면 이후 visited index 에 대해 연결된 node들의 visited index는 True로 변경되므로 연결개수를 하나씩 늘려줄 수 있다

print(cnt)