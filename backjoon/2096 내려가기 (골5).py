import sys
input = sys.stdin.readline

N = int(input().rstrip())
score_min = [[0] * 3 for _ in range(2)]
score_max = [[0] * 3 for _ in range(2)]

# DP 풀이
# 어떤 행 row에 대해, 0열로 도착한다고 가정할 때 최대값은
# row-1 행의 0열과 1열 중 최대값에다 row행의 0열 값을 더한 값이다.
# row행의 1열은 row-1행의 0열, 1열, 2열을 대상으로 위 논리를 수행한다.
# row행의 2열은 row-1행의 1열, 2열을 대상으로 위 논리를 수행한다.
# 이전 행과 다음 행의 정보만 표현하면 충분하므로, 메모리 최적화를 위해
# DP 리스트는 두 개의 행으로 구성했다.
for _ in range(N):
    nums = [*map(int, input().rstrip().split())]

    for i in range(3):
        score_min[1][i] = score_min[0][i] + nums[i]
        score_max[1][i] = score_max[0][i] + nums[i]
    
    score_min[1][0] = min(score_min[1][0], score_min[0][1] + nums[0])
    score_min[1][1] = min(score_min[1][1], score_min[0][0] + nums[1], score_min[0][2] + nums[1])
    score_min[1][2] = min(score_min[1][2], score_min[0][1] + nums[2])

    score_max[1][0] = max(score_max[1][0], score_max[0][1] + nums[0])
    score_max[1][1] = max(score_max[1][1], score_max[0][0] + nums[1], score_max[0][2] + nums[1])
    score_max[1][2] = max(score_max[1][2], score_max[0][1] + nums[2])

    for i in range(3):
        score_min[0][i] = score_min[1][i]
        score_max[0][i] = score_max[1][i]

print(max(score_max[1]), min(score_min[1]))
