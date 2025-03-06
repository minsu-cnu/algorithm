import sys
input = sys.stdin.readline

N, R = map(int, input().rstrip().split())

# 막대를 1개, 2개, 3개, ... 한 개씩 늘려가면서 가능한 쌍의 개수를 구해봄
# 이 때, 막대를 1개씩 늘릴 때, 최대한 종류 별로 홀수개를 최대한 유지하는
# 방향으로 늘려감. 이런 식으로 쭉 구해보면서 규칙 찾기
print(2 * R - 1 + N)