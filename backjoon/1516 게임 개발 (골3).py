import sys
input = sys.stdin.readline

N = int(input().rstrip())
edges = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
costs = [0] * (N + 1)

# 위상 정렬
for obj in range(1, N + 1):
    line = [*map(int, input().rstrip().split())]
    cost, pre_objs = line[0], line[1:]
    costs[obj] = cost

    for pre_obj in pre_objs[:-1]:
        edges[pre_obj].append(obj)
        in_degree[obj] += 1

# 최초 건설이 가능한 건물부터 탐색
objs_possible = [obj for obj in range(1, N + 1) if in_degree[obj] == 0]

# DP 메모이제이션 리스트
result = costs.copy()

# 위상 정렬한 그래프 순회
while objs_possible:
    obj = objs_possible.pop()

    for obj_post in edges[obj]:
        in_degree[obj_post] -= 1

        # 특정 건물의 건설 최소 시간(결과값)은, "선행 건물들의 각각의 건설 최소 시간들" 중에서의
        # 최대값에, 자기 자신의 건설 소요 시간을 더한 값이다. (DP 점화식)
        result[obj_post] = max(result[obj_post], result[obj] + costs[obj_post])
        
        if in_degree[obj_post] == 0:
            objs_possible.append(obj_post)

print(*result[1:], sep = "\n")
