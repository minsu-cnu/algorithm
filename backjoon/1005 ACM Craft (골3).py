import sys
from collections import deque
input = sys.stdin.readline

# DP[i] = max(DP[선행 노드]들) + costs[i]

for _ in range(int(input().rstrip())):
    N, K = map(int, input().strip().split())
    costs = [0] + [*map(int, input().strip().split())]
    edges = [[] for _ in range(N + 1)]

    in_degree = [0] * (N + 1)

    # edge 및 진입 차수 기록
    for _ in range(K):
        pre, post = map(int, input().strip().split())
        edges[pre].append(post)
        in_degree[post] += 1

    DP = [0] * (N + 1)
    dq = deque()
    
    # 진입 차수 0인 노드들 덱에 넣기
    for v in range(1, N + 1):
        if in_degree[v] == 0:
            dq.append(v)
            DP[v] = costs[v]
    
    W = int(input().strip())

    # DP 메모이제이션을 채워주기 위해, 위상 정렬 순서에 기반하여 탐색 및 갱신 수행
    while dq:
        pre_v = dq.popleft()

        for post_v in edges[pre_v]:
            DP[post_v] = max(DP[post_v], DP[pre_v] + costs[post_v])
            in_degree[post_v] -= 1

            if in_degree[post_v] == 0:
                dq.append(post_v) 
    
    print(DP[W])

