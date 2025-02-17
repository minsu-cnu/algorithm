import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
costs = [[sys.maxsize] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    costs[a][b] = 0

for mid in range(N + 1):
    for start in range(N + 1):
        for end in range(N + 1):
            cal_cost = costs[start][mid] + costs[mid][end]

            if cal_cost < costs[start][end]:
                costs[start][end] = cal_cost

result = 0
for student in range(1, N + 1):
    count = 0
    for other in range(1, N + 1):
        if other == student:
            continue
        
        if costs[student][other] == 0 or costs[other][student] == 0:
            count += 1
    
    if count == N - 1:
        result += 1

print(result)