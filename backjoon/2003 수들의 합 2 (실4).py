import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = [0] + [*map(int, input().strip().split())]
pre_sum = [0] * (N + 1)

for i in range(1, N + 1):
    pre_sum[i] = pre_sum[i-1] + arr[i]

left_idx = 1
right_idx = 1
result = 0

while right_idx <= N:
    sub_sum = pre_sum[right_idx] - pre_sum[left_idx - 1]

    if sub_sum == M:
        result += 1
        left_idx += 1
        right_idx += 1
    elif sub_sum < M:
        right_idx += 1
    else:
        left_idx += 1

print(result)

