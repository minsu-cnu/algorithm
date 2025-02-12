import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = sorted([*map(int, input().rstrip().split())])
result = 0

for i in range(N):
    num = nums[i]
    nums_partial = nums[:i] + nums[i + 1:]
    
    left_idx = 0
    right_idx = len(nums_partial) - 1

    while left_idx < right_idx:
        sum_two_num = nums_partial[left_idx] + nums_partial[right_idx]
        if sum_two_num == num:
            result += 1
            break
        elif sum_two_num < num:
            left_idx += 1
        else:
            right_idx -= 1

print(result)
