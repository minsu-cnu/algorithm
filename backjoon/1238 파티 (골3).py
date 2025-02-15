import sys, heapq
input = sys.stdin.readline

N, M, X = map(int, input().rstrip().split())

edges = [[] for _ in range(N + 1)]

for _ in range(M):
    start_v, end_v, cost = map(int, input().rstrip().split())
    edges[start_v].append((end_v, cost))

# costs[출발 마을][도착 마을]
costs = [[sys.maxsize] * (N + 1) for _ in range(N + 1)]

# 다익스트라를 N번 돌려서 모든 쌍의 최단 거리 구하기
# 희소 그래프에 가까우므로, 이 방식이 플로이드-워셜을 쓰는 것보다 성능 상 유리함
for start_v in range(1, N + 1):
    hq = [(0, start_v)]
    costs[start_v][start_v] = 0

    while hq:
        cur_cost, cur_v = heapq.heappop(hq)

        if costs[start_v][cur_v] < cur_cost:
            continue

        for adj_v, cost in edges[cur_v]:
            cal_cost = costs[start_v][cur_v] + cost

            if cal_cost < costs[start_v][adj_v]:
                costs[start_v][adj_v] = cal_cost
                heapq.heappush(hq, (cal_cost, adj_v))

result = 0
for student in range(1, N + 1):
    result = max(result, costs[student][X] + costs[X][student])

print(result)

