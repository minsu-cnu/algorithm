import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [*map(int, input().strip().split())]

# 초기 비교 쌍 idx 위치
left_init, right_init = -2, -1

# 오른쪽부터 순회하여 오름차순 쌍을 최초 발견했을 때 왼쪽 것 idx
swap_left = -1

# 오름차순 쌍이 하나라도 존재하는지 여부
is_finded = False

# 오름차순 쌍을 오른쪽부터 쭉 찾기
for step in range(N-1):
    left_idx = left_init - step
    right_idx = right_init - step

    if arr[left_idx] < arr[right_idx]:
        is_finded = True
        swap_left = left_idx
        break

if not is_finded:
    print(-1)
else:
    # swap_left보다 큰 원소를 맨 오른쪽 원소부터 순회하며 다시 찾기
    # 발견하면 그 것과 swap 후, 최초 오름차순 쌍의 오른쪽 원소 idx 자리부터 맨 오른쪽 끝까지 오름차순 정렬
    for idx in range(0, swap_left, -1):
        check_right = right_init + idx

        if arr[swap_left] < arr[check_right]:
            arr[swap_left], arr[check_right] = arr[check_right], arr[swap_left]
            arr = arr[:swap_left+1] + sorted(arr[swap_left+1:])
            break

    print(*arr)