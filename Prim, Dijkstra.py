# PRIM
import sys
N = 7
s = 0
g = [None] * N
g[0] = [(1, 9), (2, 10)]                                # 입력 그래프의 인접 리스트
g[1] = [(0, 9), (3, 10), (4, 5), (6, 3)]                # 입력 그래프의 인접 리스트
g[2] = [(0, 10), (3, 9), (4, 7), (5, 2)]                # 입력 그래프의 인접 리스트
g[3] = [(1, 10), (2, 9), (5, 4), (6, 8)]                # 입력 그래프의 인접 리스트
g[4] = [(1, 5), (2, 7), (6, 1)]                         # 입력 그래프의 인접 리스트
g[5] = [(2, 2), (3, 4), (6, 6)]                         # 입력 그래프의 인접 리스트
g[6] = [(1, 3), (3, 8), (4, 1), (5, 6)]                 # 입력 그래프의 인접 리스트

visited =[False] * N
D = [sys.maxsize] * N           # 각 원소를 최댓값으로
D[s] = 0
previous = [None] * N           # 트리 간선을 추출하기 위해
previous[s] = s

for k in range(N):
    m = -1                                          #  m = min_vertex
    min_value = sys.maxsize
    for j in range(N):
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j                                   # line 21~26 방문 안된 정점들의 D 원소들 중에서 최솟값을 가진 정점 m 찾기
    visited[m] = True

    for w, wt in list(g[m]):                        # 정점 m에 인접한 정점 w와 간선 (m, w)의 가중치 wt에 대해
        if not visited[w]:
            if wt < D[w]:
                D[w] = wt
                previous[w] = m
print('최소신장트리: ', end='')
mst_cost = 0
for i in range(1, N):
    print('(%d, %d)'% (i, previous[i]), end='')
    mst_cost += D[i]
print('\n최소신장트리 가중치: ', mst_cost)


# Dijkstra
import sys
N = 8
s = 0
g = [None] * N
g[0] = [(1, 1), (3, 2)]
g[1] = [(0, 1), (2, 4), (3, 3), (4, 1), (5, 6)]
g[2] = [(1, 4), (5, 1), (6, 1), (7, 2)]
g[3] = [(0, 2), (1, 3), (4, 5)]
g[4] = [(1, 1), (3, 5), (6, 2)]
g[5] = [(1, 6), (2, 1), (7, 9)]
g[6] = [(2, 1), (4, 2), (7, 1)]
g[7] = [(2, 2), (5, 9), (6, 1)]

visited = [False] * N
D = [sys.maxsize] * N   # 각 원소를 최댓값으로
D[s] = 0
previous = [None] * N   # 최단 경로 추출을 위해
previous[s] = s         # line 55 ~ 59 초기화

for k in range(N):
    m = -1                                          # m = min_vertex
    min_value = sys.maxsize
    for j in range(N):
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j                                   # line 62~67 방문 안된 정점들의 D 원소들 중에서 최솟값을 가진 정점 m 찾기
    visited[m] = True
    for v, wt in list(g[m]):                        # 정점 m에 인접한 v와 (m, v)의 가중치 wt에 대해
        if not visited[v]:
            if D[m]+wt < D[v]:
                D[v] = D[m] + wt                    # D[v] 갱신: 간선완화
                previous[v] = m                     # D[V]가 정점 m 때문에 갱신되었음을 기록

print('정점', s, '(으)로부터 최단거리:')
for i in range(N):
    if D[i] == sys.maxsize:
        print(s, '와(과) ', i, ' 사이에 경로 없음.')
    else:
        print('[%d, %d]' % (s, i), '=', D[i])

print('\n정점 ', s, '(으)로부터의 최단 경로')
for i in range(N):
    back = i
    print(back, end='')
    while back != s:
        print(' <-', previous[back], end='')
        back = previous[back]
    print()