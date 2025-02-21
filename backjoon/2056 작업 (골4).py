import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
costs = [0] * (N + 1)
edges = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for job in range(1, N + 1):
    line = [*map(int, input().rstrip().split())]
    costs[job] = line[0]
    pre_jobs = line[2:]

    for pre_job in pre_jobs:
        edges[pre_job].append(job)
        in_degree[job] += 1

result = costs.copy()
zero_in_degree = deque([job for job in range(1, N + 1) if in_degree[job] == 0])

while zero_in_degree:
    job = zero_in_degree.popleft()

    for post_job in edges[job]:
        result[post_job] = max(result[post_job], result[job] + costs[post_job])
        in_degree[post_job] -= 1

        if in_degree[post_job] == 0:
            zero_in_degree.append(post_job)

print(max(result))

