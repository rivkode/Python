N = 4
graph = [[] for _ in range(N+1)]

for _ in range(5):
    a, b = map(int, (input().split()))
    graph[a].append(b)
    graph[b].append(a)

print(graph)