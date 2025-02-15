import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

edges = [[] for _ in range(N + 1)]

for _ in range(M):
    start_v, end_v, distance = map(int, input().rstrip().split())
    edges[start_v].append((end_v, distance))

START, END = map(int, input().rstrip().split())

hq = [(0, START)]
distances = [sys.maxsize] * (N + 1)
distances[START] = 0

while hq:
    distance, v = heapq.heappop(hq)

    if distances[v] < distance:
        continue

    for adj_v, cost in edges[v]:
        cal_distance = distance + cost

        if cal_distance < distances[adj_v]:
            distances[adj_v] = cal_distance
            heapq.heappush(hq, (cal_distance, adj_v))

print(distances[END])