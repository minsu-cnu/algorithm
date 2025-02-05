import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().strip().split())
arr = [*map(int, input().strip().split())]
result = 0

for partial_size in range(1, N + 1):
    for partial_arr in combinations(arr, partial_size):
        if sum(partial_arr) == S:
            result += 1

print(result)