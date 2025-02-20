import sys
from collections import deque
input = sys.stdin.readline

# 로봇이 분열되는 지점은 S와 K임. 얘네를 노드로 정의 (로봇의 출발 포인트들이 됨)
# 그래서 예를 들어 다른 노드들에서 P 노드까지 갈 때의 최소 가중치는
# 다른 노드와 P 노드까지의 경로 가중치 합 중 최소임.
# 위 원리에 맞게, 모든 노드(S, K)끼리 서로에 대한 가능한 edge를 모두 구하고,
# 그걸로 최소 신장 트리를 만들면 그 가중치의 합이 결과값
# 이 때 edge는, 노드 P에서 노드 P까지의 최단 경로로 정의함

# (x, y) 로부터 모든 S 또는 K 좌표까지의 "직접"적인 edge를 구하는 함수
def find_edges(x, y):
    dq = deque([(x, y)])
    visited = [[-1] * N for _ in range(N)]
    visited[x][y] = 0

    while dq:
        cur_x, cur_y = dq.popleft()

        if points[cur_x][cur_y] == True and (x, y) != (cur_x, cur_y):
            edges.append((visited[cur_x][cur_y], x, y, cur_x, cur_y))
            continue

        for i in range(4):
            adj_x = cur_x + dx[i]
            adj_y = cur_y + dy[i]

            if maze[adj_x][adj_y] == "1":
                continue

            if visited[adj_x][adj_y] == -1:
                visited[adj_x][adj_y] = visited[cur_x][cur_y] + 1
                dq.append((adj_x, adj_y))

# 유니온 파인드
def find(x, y):
    if parent[x][y][0] < 0:
        return [x, y]
    
    parent[x][y] = find(*parent[x][y])
    return parent[x][y]

def union(x, y, z, w):
    root_x, root_y = find(x, y)
    root_z, root_w = find(z, w)

    if (root_x, root_y) == (root_z, root_w):
        return False
    
    if parent[root_x][root_y][0] < parent[root_z][root_w][0]:
        parent[root_z][root_w] = [root_x, root_y]
        parent[root_x][root_y][0] -= 1
    elif parent[root_x][root_y][0] > parent[root_z][root_w][0]:
        parent[root_x][root_y] = [root_z, root_w]
        parent[root_z][root_w][0] -= 1
    else:
        parent[root_x][root_y] = [root_z, root_w]
        parent[root_z][root_w][0] -= 1
    
    return True
            
N, M = map(int, input().rstrip().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

maze = []
for _ in range(N):
    maze.append(list(input().rstrip()))

# S 또는 K인 좌표들과 그 개수 구하기
points = [[False] * N for _ in range(N)]
point_count = 0
for x in range(N):
    for y in range(N):
        if maze[x][y] in "SK":
            points[x][y] = True
            point_count += 1

# S와 K들 사이의 가능한 모든 edge 구하기
edges = []
for x in range(N):
    for y in range(N):
        if points[x][y]:
            find_edges(x, y)

# 구한 edge들을 기반으로 MST 구하기
edges.sort()
parent = [[[-1, -1]] * N for _ in range(N)]
result = 0
link_count = 0

for c, x, y, z, w in edges:
    if union(x, y, z, w):
        result += c
        link_count += 1
    
    if link_count == point_count - 1:
        break

if link_count == point_count - 1:
    print(result)
else:
    print(-1)