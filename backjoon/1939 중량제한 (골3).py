import sys
from collections import deque
input = sys.stdin.readline

# 무게 cost_of_object 만큼의 물건을 목표 섬까지 이동시킬 수 있는지 BFS로 판별
def deliver_object(cost_of_object, START, END, N):
    dq = deque([START])
    visited = [False] * (N + 1)
    visited[START] = True

    while dq:
        cur_v = dq.popleft()

        for adj_v, cost in edges[cur_v]:
            if cost_of_object <= cost and not visited[adj_v]:
                visited[adj_v] = True
                dq.append(adj_v)
    
    return visited[END]

N, M = map(int, input().rstrip().split())
edges = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().rstrip().split())
    edges[A].append((B, C))
    edges[B].append((A, C))

START, END = map(int, input().rstrip().split())

left_cost = 1
right_cost = 1000000000

# 옮길 물건의 가능한 무게의 최대치를 이분 탐색
while left_cost <= right_cost:
    mid_cost = (left_cost + right_cost) // 2

    if deliver_object(mid_cost, START, END, N):
        left_cost = mid_cost + 1
    else:
        right_cost = mid_cost - 1

print(right_cost)