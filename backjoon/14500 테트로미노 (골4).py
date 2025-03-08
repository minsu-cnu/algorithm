import sys, copy
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]
result = 0

# 회전, 대칭을 고려하여 총 19개(중복 제거 처리 후)의 필터를 가능한 위치에 모두 돌면서
# 그 때의 합 중 최대값 구하기
# 시간복잡도상 완탐 가능할 듯

# 5가지 모양 기본 필터 (첫 튜플은 행과 열을 의미, 그 이후부턴 좌표 튜플)
filter = [[(1, 4), [0, 0], [0, 1], [0, 2], [0, 3]],
          [(2, 2), [0, 0], [0, 1], [1, 0], [1, 1]],
          [(3, 2), [0, 0], [1, 0], [2, 0], [2, 1]],
          [(3, 2), [0, 0], [1, 0], [1, 1], [2, 1]],
          [(2, 3), [0, 0], [0, 1], [0, 2], [1, 1]]]

# 기본 필터를 회전, 대칭한 필터도 모두 구해주기
for filter_idx in range(len(filter)):
    filter_info = filter[filter_idx]
    row_range, col_range = filter_info[0]
    filter_cdns = filter_info[1:]

    # 3번 회전 (오른쪽으로 회전, 행은 이전의 열과 같고, 열은 "회전 후 최대 열 인덱스 - 회전 전 행 - 1")
    rotate_row_range, rotate_col_range = row_range, col_range
    rotate_cdns = copy.deepcopy(filter_cdns)

    for rotate_count in range(3):
        rotate_row_range, rotate_col_range = rotate_col_range, rotate_row_range

        for cdn_idx in range(len(rotate_cdns)):
            row, col = rotate_cdns[cdn_idx]
            rotate_row = col
            rotate_col = rotate_col_range - row - 1
            rotate_cdns[cdn_idx] = [rotate_row, rotate_col]
        
        filter.append([(rotate_row_range, rotate_col_range)] + rotate_cdns)
    
    # 좌우 대칭 (상하 대칭을 안하는 이유는, 상하 대칭은 좌우 대칭 후 180도 회전과 같음)
    rotate_row_range, rotate_col_range = row_range, col_range
    sym_cdns = []
    for i in range(len(filter_cdns)):
        origin_row, origin_col = filter_cdns[i]
        sym_row = origin_row
        sym_col = col_range - origin_col - 1
        sym_cdns.append([sym_row, sym_col])
    
    filter.append([(row_range, col_range)] + sym_cdns)

    rotate_cdns = copy.deepcopy(sym_cdns)
    
    # 3번 회전
    for rotate_count in range(3):
        rotate_row_range, rotate_col_range = rotate_col_range, rotate_row_range

        for cdn_idx in range(len(rotate_cdns)):
            row, col = rotate_cdns[cdn_idx]
            rotate_row = col
            rotate_col = rotate_col_range - row - 1
            rotate_cdns[cdn_idx] = [rotate_row, rotate_col]
        
        filter.append([(rotate_row_range, rotate_col_range)] + rotate_cdns)

# 중복 필터 제거
dup_idx = set()
for filter_idx in range(len(filter)):
    for comp_filter_idx in range(filter_idx + 1, len(filter)):
        is_equal = True
        filter_cdns = sorted(filter[filter_idx][1:])
        comp_filter_cdns = sorted(filter[comp_filter_idx][1:])

        for i in range(4):
            if filter_cdns[i][0] != comp_filter_cdns[i][0] or filter_cdns[i][1] != comp_filter_cdns[i][1]:
                is_equal = False
                break

        if is_equal:
            dup_idx.add(comp_filter_idx)

# 앞서 구한 모든 필터들을 가능한 모든 위치로 순회시키면서 결과값 찾기
for filter_idx in range(len(filter)):
    if filter_idx in dup_idx:
        continue

    filter_info = filter[filter_idx]
    filter_row_range, filter_col_range = filter_info[0]
    filter_cdns = filter_info[1:]

    for start_row in range(N - filter_row_range + 1):
        for start_col in range(M - filter_col_range + 1):
            area_sum = 0

            for filter_row, filter_col in filter_cdns:
                target_row = start_row + filter_row
                target_col = start_col + filter_col
                area_sum += board[target_row][target_col]

            result = max(result, area_sum)

print(result)