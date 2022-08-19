def dfs(start): #전에 방문한 노드보다 큰 노드만 방문하기 위해 start값으로 파라미터 전달
    if len(s) == m: # 만약 s의 길이가 구해야하는 길이와 같을 경우
        print(*s) # s를 출력 후 함수 빠져나옴
        return
    for i in range(start+1, n+1): # 전에 방문한 노드 +1 부터 반복 - 오름차순을 위함
        visited[i] = True # 방문처리
        s.append(i) # 오름차순으로 입력될 i 를 s 리스트에 추가
        dfs(i) # 방문한 노드를 파라미터로 전달하여 이것보다 큰 것만 방문하게 한다 - 오름차순을 위함
        s.pop() # 전 상태로 되돌리기 위해 pop
        visited[i] = False # 전 상태로 돌리기 위해 다시 미 방문처리

n, m = map(int, input().split())
s = [] # 답을 출력할 리스트 생성
visited = [False] * (n+1)

dfs(0) # 0부터 시작