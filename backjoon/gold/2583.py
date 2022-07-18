from collections import deque
m, n, k = list(map(int, input().split()))


def bfs(graph, x, y, visited_list):
    queue = deque([x, y])
    visited_list[x, y] = True

    while queue:
        v = queue.popleft()
        for i in graph[x, y]:
            if not visited_list[i]:
                queue.append(i)
                visited_list[i] = True

array_list = []
for j in range(n):
    array_list.append(0)
graph = []
for i in range(m):
    graph.append(array_list)
print(graph)


def draw(graph, x1, y1, x2, y2):

    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[j][i] = 1

# print(graph)


for _ in range(k):
    visited_list = []
    coordinate = list(map(int, input().split()))
    draw(graph, coordinate[0], coordinate[1], coordinate[2], coordinate[3])

    bfs(graph, coordinate[0], coordinate[1], visited_list)


    print(graph)

