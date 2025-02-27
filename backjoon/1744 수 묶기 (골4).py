import sys
input = sys.stdin.readline

# 음수는 절대값이 큰 음수끼리 묶고, 한 개만 남았다면 0과 묶기
# 0이 없거나 음수 짝이 더 이상 없다면, 하나 남은 그 음수는 그대로 두기
# 양수는 서로 가장 큰 것끼리 그리디하게 묶기
# 단, 1은 어떤 수와도 묶지 않고 그대로 두기

N = int(input().rstrip())
arr = sorted([int(input().rstrip()) for _ in range(N)])
result = 0

if N == 1:
    result = arr[0]
else:
    left_idx = 0
    right_idx = 1
    flag = False

    while right_idx < N:
        left = arr[left_idx]
        right = arr[right_idx]

        if left < 0:
            if right < 0:
                result += left * right
                left_idx += 2
                right_idx += 2
            elif right == 0:
                left_idx += 2
                right_idx += 2
            elif right > 0:
                result += left
                left_idx += 1
                right_idx += 1
        elif left == 0:
            left_idx += 1
            right_idx += 1
        elif left == 1:
            result += left
            left_idx += 1
            right_idx += 1
        elif left > 1:
            if (N - left_idx) % 2 and not flag:
                result += left
                left_idx += 1
                right_idx += 1
                flag = True
            else:
                result += left * right
                left_idx += 2
                right_idx += 2

    if left_idx < N:
        result += arr[left_idx]

print(result)

