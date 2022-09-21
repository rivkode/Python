import time
import sys
input = sys.stdin.readline

start_time = time.time()
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k+1)) * k
count += m%(k+1)

result = 0
result += (count) * first
result += (m-count) * second
end_time = time.time()
print(result)
print("time", end_time - start_time)