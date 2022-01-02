adj_list = [[1], [3,4], [0,1], [6], [5], [7], [7], [8], []] # 그래프 인접리스트
N = len(adj_list)
visited = [None] * N    # 정점 방문 여부 확인 용
s = []      # 위상정렬 결과 리스트 초기화

def dfs(v):
    visited[v] = True
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)
    s.append(v)             # 정점 v의 모든 인접한 정점들이 방문되었으므로 정점 v 추가

for i in range(N):
    if not visited[i]:
        dfs(i)              # dfs() 호출로 시작
s.reverse()                 # s의 역순으로 위상정렬 결과를 얻음
print('위상정렬:')
print(s)




# Kruskal
weights = [(0, 1, 9), (0, 2, 10), (1, 3, 10), (1, 4, 5),
           (1, 6, 3), (2, 3, 9), (2, 4, 7), (2, 5, 2),
           (3, 5, 4), (3, 6, 8), (4, 6, 1), (5, 6, 6)]          # 입력 그래프 (간선의 두 정점, 가중치)
weights.sort(key = lambda t: t[2])
mst = []
N = 7
p = [] * N  # 상호 배타적 집합
for i in range(N):
    p.append(i)     # 각 정점 자신이 집합의 대표(루트)

def find(u):         # find 연산
    if u != p[u]:
        p[u] = find(p[u])   # 경로 압축
    return p[u]

def union(u, v):     # union 연산
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1    # 임의로 root2가 root1의 부모가 됨

tree_edges = 0
mst_cost = 0
while True:
    if tree_edges == N-1:
        break
    u, v, wt = weights.pop(0)       # 다음 최소 가중치를 가진 간선 가져오기
    if find(u) != find(v):          # u와 v가 서로 다른 집합에 속해 있으면
        union(u, v)
        mst.append((u, v))          # 트리에 (u, v) 추가
        mst_cost += wt
        tree_edges += 1

print('최소신장트리: ', end='')
print(mst)
print('최소신장트리 가중치:', mst_cost)