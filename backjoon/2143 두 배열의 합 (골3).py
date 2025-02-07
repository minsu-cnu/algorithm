import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input().strip())

n = int(input().strip())
A = [0] + [*map(int, input().strip().split())]
pre_sum_of_A = [0] * (n + 1)

m = int(input().strip())
B = [0] + [*map(int, input().strip().split())]
pre_sum_of_B = [0] * (m + 1)

for i in range(1, n + 1):
    pre_sum_of_A[i] = pre_sum_of_A[i - 1] + A[i]

for i in range(1, m + 1):
    pre_sum_of_B[i] = pre_sum_of_B[i - 1] + B[i]

result = 0

# key : A의 부 배열의 합
# value : 해당 합을 갖는 부 배열의 경우의 수
count_sub_sum_of_A = defaultdict(int)

# 위 딕셔너리 채우기
for size in range(1, n + 1):
    for left_idx in range(1, n - size + 2):
        right_idx = left_idx + size - 1
        sub_sum = pre_sum_of_A[right_idx] - pre_sum_of_A[left_idx - 1]

        count_sub_sum_of_A[sub_sum] += 1

# B의 모든 부 배열을 순회하면서, 현재 단계 부 배열의 합이 p라고 할 때,
# A의 부 배열 중 합이 T - p 인 것이 q개이면,
# result에 q를 더해준다.
for size in range(1, m + 1):
    for left_idx in range(1, m - size + 2):
        right_idx = left_idx + size - 1
        sub_sum = pre_sum_of_B[right_idx] - pre_sum_of_B[left_idx - 1]

        result += count_sub_sum_of_A[T - sub_sum]

print(result)

