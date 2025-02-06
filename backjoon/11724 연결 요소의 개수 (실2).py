import sys
input = sys.stdin.readline

def DFS(cur_v):
    stack = [cur_v]
    visited[cur_v] = True

    while stack:
        cur_v = stack.pop()

        for adj_v in edges[cur_v]:
            if not visited[adj_v]:
                visited[adj_v] = True
                stack.append(adj_v)

N, M = map(int, input().strip().split())
edges = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
result = 0

for _ in range(M):
    u, v = map(int, input().strip().split())

    edges[u].append(v)
    edges[v].append(u)

for v in range(1, N + 1):
    if not visited[v]:
        DFS(v)
        result += 1

print(result)