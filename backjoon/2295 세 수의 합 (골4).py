import sys
input = sys.stdin.readline

# arr[x] + arr[y] = arr[k] - arr[z] 를 만족하는 arr[k]의 최대값 구하기

N = int(input().rstrip())
arr = sorted([int(input().rstrip()) for _ in range(N)])
two_sum = set()
result = 0

for x in range(N):
    for y in range(N):
        two_sum.add(arr[x] + arr[y])

for k in range(N - 1, -1, -1):
    for z in range(k - 1, -1, -1):
        two_sub = arr[k] - arr[z]

        if two_sub in two_sum:
            result = max(result, arr[k])

print(result)