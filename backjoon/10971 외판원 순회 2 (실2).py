import sys
input = sys.stdin.readline

# start_city : 최초 출발 도시
# cur_city : 현재 방문 중인 도시
# cumulative_cost : 최초 출발 도시부터 현재까지의 누적 비용
# lowest_cost : 현재 시점까지, 순회를 끝마쳤던 경우들에 대해 가장 최소 비용 기록
# go_count : 최초 출발 도시를 포함하여 현재 방문 도시까지의 누적 방문 횟수
# 리턴 : cur_city로부터 인접한 방문 가능 도시로 탐색을 모두 수행한 후의 lowest_cost
def DFS(start_city, cur_city, N, cumulative_cost, lowest_cost, go_count):
    # 모든 도시를 방문했을 때(마지막 도시 방문), 최초 출발 도시로의 경로가 있다면,
    # 현재 루트의 총 경로 비용과 lowest_cost를 비교하여 갱신
    if go_count == N:
        if W[cur_city][start_city] != 0:
            return min(lowest_cost, cumulative_cost + W[cur_city][start_city])
        else:
            return lowest_cost
    
    # 현재 도시 기준 인접 도시로 탐색 수행하며 lowest_cost를 갱신해나감
    for adj_city in range(N):
        adj_cost = W[cur_city][adj_city]
        if not visited[adj_city] and adj_cost != 0:
            # 다음 인접 도시로 갈 때 이미 비용이 lowest_cost를 넘어버린다면
            # 그 루트로의 탐색을 하지 않음 (백트래킹)
            if cumulative_cost + adj_cost < lowest_cost:
                visited[adj_city] = 1
                lowest_cost = DFS(start_city, adj_city, N, cumulative_cost + adj_cost, lowest_cost, go_count + 1)
                visited[adj_city] = 0
    
    return lowest_cost

N = int(input().strip())
W = []
visited = [0]*N

for _ in range(N):
    W.append([*map(int, input().strip().split())])

result = sys.maxsize
# 모든 도시가 출발 도시 후보임. 각 경우 모두 탐색
for city in range(N):
    visited[city] = 1
    result = min(result, DFS(city, city, N, 0, sys.maxsize, 1))

print(result)