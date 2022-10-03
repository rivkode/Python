T = int(input())

def buceo(k, n):
    people = []
    for i in range(1, n+1):
        people.append(i)
    for _ in range(k):
        for y in range(1, n):
            people[y] += people[y-1]
    return people[-1]

for i in range(T):
    k = int(input())
    n = int(input())
    print(buceo(k, n))