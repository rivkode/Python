import sys
input = sys.stdin.readline

n = int(input())
lst = []
answer = [0, 0]

for _ in range(n):
    lst.append(input().rstrip().split(' '))
print(lst)

def paper(lst):
    length = int(len(lst)/2)
    if length < 0:
        return 0
    lst1 = []
    lst2 = []
    lst3 = []
    lst4 = []

    for i in range(1, 5):
        for j in range(length):
            lst[i].append(lst[j][0:length])
    return paper(lst1), paper(lst2), paper(lst3), paper(lst4)

paper(lst)


