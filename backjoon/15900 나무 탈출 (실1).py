import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())

# 총 이동 횟수가 홀수개이면 반드시 승리

edges = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

dq = deque([1])
moves = [0] * (N + 1)
moves[1] = 1

total_move = 0

while dq:
    cur_v = dq.popleft()

    is_leaf = True
    for adj_v in edges[cur_v]:
        if not moves[adj_v]:
            moves[adj_v] = moves[cur_v] + 1
            dq.append(adj_v)
            is_leaf = False
    
    if is_leaf:
        total_move += moves[cur_v] - 1

print("Yes" if total_move % 2 != 0 else "No")

