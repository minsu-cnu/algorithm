import sys

N, K = map(int, sys.stdin.readline().strip().split())
A = [*map(int, sys.stdin.readline().strip().split())]

print(sorted(A)[K-1])