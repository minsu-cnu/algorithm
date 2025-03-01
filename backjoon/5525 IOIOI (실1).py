import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
S = input().rstrip()

idx = 0
acc_IOI = 0
result = 0

# 선형적으로 순회하면서, IOI 를 찾는다.
# IOI를 발견하면 그 오른쪽으로 idx를 옮기는게 아닌,
# IOI 에서 세 번째 위치에 있는 I 위치로 idx를 옮겨서,
# 다시 IOI를 검사하도록 한다.
# 이런 식으로 탐색했을 때, 연속으로 IOI를 체크한 횟수로
# P인지 여부를 판정한다.
# 시간복잡도는 O(N^3)

while idx < M:
    if S[idx:idx + 3] == "IOI":
        acc_IOI += 1
        idx += 2

        if acc_IOI == N:
            result += 1
            acc_IOI -= 1

    else:
        acc_IOI = 0
        idx += 1

print(result)