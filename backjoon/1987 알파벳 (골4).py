import sys
input = sys.stdin.readline

R, C = map(int, input().strip().split())
board = []
drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

for _ in range(R):
    board.append(list(input().strip()))

# 현재 좌표 기준 인접 좌표들 DFS 탐색 후, 인접 탐색 결과값들과 내 위치까지의
# 결과값 중 최대값을 리턴
def DFS(cur_r, cur_c):
    result = len(path)

    # 이거 제너레이터로 하면 TLE 나니까 이 방식으로 해야됨
    for i in range(4):
        adj_r = cur_r + drow[i]
        adj_c = cur_c + dcol[i]

        if not (0 <= adj_r < R and 0 <= adj_c < C):
            continue
        
        if board[adj_r][adj_c] in path:
            continue

        path.add(board[adj_r][adj_c])
        result = max(result, DFS(adj_r, adj_c))
        path.remove(board[adj_r][adj_c])

    return result

# 집합으로 path를 기록
# 경로 길이 계산과 방문 여부 체크를 set을 통해 수행 가능
path = set(board[0][0])
print(DFS(0, 0))