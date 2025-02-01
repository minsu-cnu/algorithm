# 두 그룹으로 나누기
# 각 그룹 내 노드들은 반드시 모두 연결 (간접 연결도 가능)
# 그룹 간 인구수 차이의 최솟값 알아내기
# 두 그룹으로 못 나누면 -1 출력

def find(x):
    if parent[x] < 0:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return False
    
    if parent[x_root] < parent[y_root]:
        parent[y_root] = x_root
    elif parent[x_root] > parent[y_root]:
        parent[x_root] = y_root
    else:
        parent[x_root] = y_root
        parent[y_root] -= 1

import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input().strip()) # 노드 개수
areas = set(range(1, N+1)) # 모든 노드 넘버 집합
populations = [0] + [*map(int, input().strip().split())] # 각 노드 별 인구 수
edges = [[0]*(N+1) for _ in range(N+1)] # 엣지 정보
result = sys.maxsize

# 간선 정보 받기
for v in range(1, N+1):
    adj_v_list = [*map(int, input().strip().split())][1:]

    for adj_v in adj_v_list:
        edges[v][adj_v] = 1
        edges[adj_v][v] = 1

# 두 그룹으로 나눠지는 개수에 대해, 각 경우의 수에서 조합을 통해 가능한 그룹 분할 경우의 수 순회
for group_left_size in range(1, (N // 2) + 1):
    # 나눠진 그룹에 대한 작업
    for group_left in combinations(areas, group_left_size):
        flag_group_left_linked = True # 분할 그룹 1은 연결 요소인가
        flag_group_right_linked = True # 분할 그룹 2는 연결 요소인가
        parent = [-1]*(N+1) # 유니온 파인드를 위한 배열
        group_left = list(group_left) # 분할 그룹 1
        group_right = list(areas - set(group_left)) # 분할 그룹 2

        # 분할 그룹 1을 유니온 파인드를 통해 연결 요소 만들어보기
        for left_idx in range(len(group_left)-1):
            for right_idx in range(left_idx+1, len(group_left)):
                target_1 = group_left[left_idx]
                target_2 = group_left[right_idx]
                if edges[target_1][target_2]:
                    union(target_1, target_2)

        # 연결 요소라면 flag에는 True가 있게 될 것
        group_left_root = find(group_left[0])
        for v in group_left[1:]:
            if find(v) != group_left_root:
                flag_group_left_linked = False
                break
        
        # 위 작업을 분할 그룹 2에 대해 동일하게 수행
        for left_idx in range(len(group_right)-1):
            for right_idx in range(left_idx+1, len(group_right)):
                target_1 = group_right[left_idx]
                target_2 = group_right[right_idx]
                if edges[target_1][target_2]:
                    union(target_1, target_2)

        group_right_root = find(group_right[0])
        for v in group_right[1:]:
            if find(v) != group_right_root:
                flag_group_right_linked = False
                break
        
        # 두 그룹 모두 연결 요소라면, 각 그룹의 인구 수 합의 차를 구한 뒤, result에 최솟값 갱신
        if flag_group_left_linked and flag_group_right_linked:
            group_left_population = sum([populations[i] for i in group_left])
            group_right_population = sum([populations[i] for i in group_right])
            result = min(result, abs(group_left_population - group_right_population))
        
if result >= sys.maxsize:
    print(-1)
else:
    print(result)

