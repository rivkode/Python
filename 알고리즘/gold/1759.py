def dfs(start):
    vowel = ["a", "e", "i", "o", "u"]

    if len(s) == c:
        if s in vowel:
            print(' '.join(map(str, s)))
        return

    for i, sec_s in enumerate(sec_lst, start = start+1):

        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs(start)
        s.pop()
        visited[i] = False

l, c = map(int, input().split())
sec_lst = list(map(str, input().split()))
sec_lst.sort()
print(sec_lst)
s = []
visited = [False] * (c+1)

dfs(sec_lst[0])