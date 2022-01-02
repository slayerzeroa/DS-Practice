# DFS(깊이 우선 탐색)
adj_list = [[2,1], [3,0], [3,0], [9,8,2,1], [5], [7,6,4], [7,5], [6,5], [3], [3]]   # 그래프 인접리스트
N = len(adj_list)
visited = [None] * N    # 정점 방문 여부 확인용

def dfs(v):
    visited[v] = True           # 정점 v 방문
    print(v, ' ', end='')
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)              # 정점 v에 인접한 정점으로 dfs() 호출

print('DFS 방문 순서: ')
for i in range(N):
    if not visited[i]:
        dfs(i)                  # dfs() 호출


# BFS(너비 우선 탐색)
adj_list = [[2,1], [3,0], [3,0], [9,8,2,1], [5], [7,6,4], [7,5], [6,5], [3], [3]]   # 그래프 인접리스트
N = len(adj_list)
visited = [None] * N    # 정점 방문 여부 확인용

def bfs(i):
    queue = []      # 큐를 리스트로 구현
    visited[i] = True
    queue.append(i)
    while len(queue) != 0:
        v = queue.pop(0)        # 큐의 맨 앞에서 제거된 정점을 v가 참조하게 함
        print(v, ' ', end='')   # 정점 v 방문
        for w in adj_list[v]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)     # v에 인접하면서 방문 안 된 정점 큐에 삽입

print('\nBFS 방문 순서:')
for i in range(N):
    if not visited[i]:
        bfs(i)          # bfs() 호출



# cc
adj_list = [[3], [6, 10], [7, 11], [0, 6, 8], [13], [14], [1, 3, 8, 10, 11], [2, 11], [3, 6, 10, 12], [13], [1, 6, 8], [2, 6, 7], [8], [4, 9], [5]] # 그래프 연결리스트
N = len(adj_list)
CCList = []
visited = [None] * N        # 정점 방문 확인용

def dfs(v):
    visited[v] = True
    cc.append(v)            # 현재 연결 성분에 정점 v 추가
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)          # 정점 v가 인접한 w로 dfs() 재귀호출

for i in range(N):
    if not visited[i]:
        cc = []             # 새로운 연결성분을 위한 초기화
        dfs(i);             # dfs 호출로 cc 만들기
        CCList.append(cc)   # 완성된 cc를 연결성분 리스트에 추가

print('\n연결성분 리스트: ')
print(CCList)