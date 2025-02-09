# 가로 1을 0개 쓰는 경우의 수, 1개 쓰는 경우의 수, ..., 최대로 쓰는 경우의 수
# 최소 = n이 홀수면 1개, 짝수면 0개
# 최대 = n개
# 각 경우에 대해, 1x2 k개를 놓는 것이 가능할 때, 경우의 수 = (k+(n-k)//2)!/k!*((n-k)//2)!
# n이 홀수라면 k는 홀수만 가능, n이 짝수라면 k는 짝수만 가능
import sys
input = sys.stdin.readline

n = int(input().rstrip())
is_odd = 1 if n % 2 != 0 else 0
factorial = [1]*(n+1)
result = 0

for i in range(1, n + 1):
    factorial[i] = factorial[i-1] * i

for k in range(is_odd, n + 1, 2):
    m = (n - k) // 2
    result += (factorial[k + m] // (factorial[k] * factorial[m])) % 10007

print(result % 10007)



