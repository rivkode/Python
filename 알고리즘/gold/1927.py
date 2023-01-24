import heapq #최소 힙 heapq를 사용
import sys
input = sys.stdin.readline

n = int(input())
pq = []

for i in range(n):
    a = int(input())
    if a != 0:
        heapq.heappush(pq, int(a))
    else:
        if len(pq) == 0:
            print(0)
        else:
            v = heapq.heappop(pq)
            print(v)