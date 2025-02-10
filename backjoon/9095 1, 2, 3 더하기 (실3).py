import sys
input = sys.stdin.readline

# DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
# 왼쪽 1 고정 후 DP[i-1]
# 왼쪽 2 고정 후 DP[i-2]
# 왼쪽 3 고정 후 DP[i-3]

DP = [1]*11
DP[2] = 2

for i in range(3, 11):
    DP[i] = DP[i-1] + DP[i-2] + DP[i-3]

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())

    print(DP[n])

