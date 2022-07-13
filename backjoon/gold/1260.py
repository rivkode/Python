# 백준 대표 dfs, bfs // 1260

from collections import deque # bfs deque 사용
import sys
input = sys.stdin.readline

# 함수로 만들기
# 전처리
# input, 과정, output 순으로 만들자


def dfs(graph, v, visited): # 깊이 우선 탐색
    visited[v] = True # 방문처리
    print(v, end=" ") # 방문한 숫자 출력
    for i in graph[v]:
        if not visited[i]: # 인접 인자가 방문처리 되지 않았다면 다시 재귀함수로 실행
            dfs(graph, i, visited)


def bfs(graph, start, visited): # 너비 우선 탐색
    queue = deque([start]) # queue 사용하여 들어온 순서대로 나가는 원리
    visited[start] = True # 방문처리
    while queue: # queue가 존재할동안 계속
        v = queue.popleft() # queue 의 가장 왼쪽을 pop
        print(v, end=' ') # pop 숫자 출력
        for i in graph[v]:
            if not visited[i]: # pop 숫자의 인접한 인자가 방문처리 되지 않을 경우
                queue.append(i) # queue 에 추가
                visited[i] = True # 방문 처리

N, M, V = (map(int, input().split())) # 조건 입력 map을 이용하여 받기

graph = [[] for _ in range(N+1)] # 최초 그래프 생성

for _ in range(M):
    a, b = map(int, (input().split()))
    graph[a].append(b) # a 번째 b 원소 추가하기
    graph[b].append(a) # 두 경우에 대해 서로 매칭시키기 위해
    graph[a].sort() # 정렬하기 - 이 부분을 하지 않아 틀렸음 !
    graph[b].sort()


visited = [False] * (N+1)
dfs(graph, V, visited)
visited = [False] * (N+1) # visited 를 사용하였으므로 사용하기 전 초기화
print()
bfs(graph, V, visited)