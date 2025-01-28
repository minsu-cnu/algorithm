import sys
from itertools import combinations
input = sys.stdin.readline

input_case = [*map(int, input().strip().split())]

k = input_case[0]
S = input_case[1:]

while k != 0:
    for nums in sorted(combinations(S, 6)):
        print(*nums)
    
    print()
    input_case = [*map(int, input().strip().split())]

    k = input_case[0]
    S = input_case[1:]

