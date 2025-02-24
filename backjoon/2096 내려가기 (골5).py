import sys
input = sys.stdin.readline

N = int(input().rstrip())
score_min = [[0] * 3 for _ in range(2)]
score_max = [[0] * 3 for _ in range(2)]

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
