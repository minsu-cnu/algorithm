import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

def BFS(row, col):
    dq = deque([(row, col)])

    while dq:
        cur_row, cur_col = dq.popleft()

        for i in range(4):
            nrow = cur_row + drow[i]
            ncol = cur_col + dcol[i]

            if not (0 <= nrow < N and 0 <= ncol < M):
                continue

            if board[nrow][ncol] == 0:
                board[nrow][ncol] = 2
                dq.append((nrow, ncol))

N, M = map(int, input().strip().split())
board = [[*map(int, input().strip().split())] for _ in range(N)]
drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]
result = 0

# 1. 0인 좌표 전부 구하기
# 2. 2인 좌표 전부 구하기
# 3. 0인 좌표들 중 3개 combination으로 뽑고 그 좌표 1로 만들기 (벽 세우기 / loop)
# 4. 2인 좌표들 전부 BFS 돌리기 (loop)
# 5. 0인 좌표 개수 구하기 (NxM 탐색)
# 6. 지도 리셋하고 3번 수행

# 0인 좌표 전부 구하기, 2인 좌표 전부 구하기
cdns_zero = []
cdns_two = []
for row in range(N):
    for col in range(M):
        if board[row][col] == 0:
            cdns_zero.append((row, col))
        elif board[row][col] == 2:
            cdns_two.append((row, col))

# 3~6번 항목 수행
for candidates in combinations(cdns_zero, 3):
    # 벽 세우기
    for row, col in candidates:
        board[row][col] = 1
    
    # 2인 좌표들 전부 BFS 돌리기
    for row, col in cdns_two:
        BFS(row, col)
    
    # 0인 좌표 개수 구하기
    count_zero = 0
    for row in range(N):
        for col in range(M):
            if board[row][col] == 0:
                count_zero += 1
    
    result = max(result, count_zero)

    # 지도 리셋
    for row, col in candidates:
        board[row][col] = 0
    
    for row in range(N):
        for col in range(M):
            if board[row][col] == 2:
                board[row][col] = 0
    
    for row, col in cdns_two:
        board[row][col] = 2

print(result)