import sys
input = sys.stdin.readline

N, r, c = map(int, input().strip().split())

# 특정 범위를 Z형 탐색
# 리턴 값 : 해당 범위 내에서 r행 c열을 몇 번째로 방문하는지 (서수는 0부터)
# 이 함수가 호출된 범위 내에 r행 c열이 반드시 있다.
def search_Z(row_start, row_end, col_start, col_end, r, c):
    # 재귀적 분할 후 탐색 박스 한 변의 길이
    resize = (row_end - row_start + 1) // 2

    # 탐색 박스가 한 칸인 경우, r행 c열이 반드시 있다고 했으니 해당 칸이 곧 목표 좌표
    # 즉 탐색 박스 내에서 0번째로 방문한 것이므로 0 리턴
    if resize == 0:
        return 0
    
    # 재귀적 분할 후, 목표 r행 c열 칸이 몇 번째 박스에 있는지 (이 때의 서수는 1부터)
    found_group_number = 0

    # 분할 후 탐색 박스들 탐색
    for row_group in range(2):
        for col_group in range(2):
            row_splited_start = row_start + resize * row_group
            row_splited_end = row_splited_start + resize - 1
            col_splited_start = col_start + resize * col_group
            col_splited_end = col_splited_start + resize - 1

            # 목표 r행 c열이 분할 탐색 박스 내에 있으면 그 박스를 재귀적으로 다시 탐색
            # 없으면 박스 카운팅 후 다음 탐색 박스 순회로 넘어감
            if row_splited_start <= r <= row_splited_end and col_splited_start <= c <= col_splited_end:
                search_group_result = search_Z(row_splited_start, row_splited_end, col_splited_start, col_splited_end, r, c)
                return (resize ** 2) * found_group_number + search_group_result

            found_group_number += 1

print(search_Z(0, 2**N - 1, 0, 2**N - 1, r, c))
