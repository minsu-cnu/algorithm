import sys
input = sys.stdin.readline

def assign_budget(limit, budget):
    sum_assigned = 0

    for request in requests:
        sum_assigned += min(limit, request)
    
    return sum_assigned <= budget


N = int(input().rstrip())
requests = [*map(int, input().rstrip().split())]
M = int(input().rstrip())

start_limit = 1
end_limit = M

while start_limit <= end_limit:
    mid_limit = (start_limit + end_limit) // 2

    if assign_budget(mid_limit, M):
        start_limit = mid_limit + 1
    else:
        end_limit = mid_limit - 1

print(min(max(requests), end_limit))