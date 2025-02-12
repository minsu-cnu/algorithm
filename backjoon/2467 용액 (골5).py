import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = [*map(int, input().rstrip().split())]

left_idx = 0
right_idx = N - 1
result = sys.maxsize
a, b = 0, 0

while left_idx < right_idx:
    sum_two_num = nums[left_idx] + nums[right_idx]

    if abs(sum_two_num) < result:
        result = abs(sum_two_num)
        a, b = nums[left_idx], nums[right_idx]

    if sum_two_num == 0:
        break
    elif sum_two_num < 0:
        left_idx += 1
    else:
        right_idx -= 1

print(a, b)