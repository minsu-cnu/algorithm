import sys
input = sys.stdin.readline

N = int(input().rstrip()) # N <= 50
parent = [*map(int, input().rstrip().split())]
target = int(input().rstrip())

# target을 포함한 서브 트리를 제거 (부모 값을 -2로 설정)
target_parents = [target]
while target_parents:
    target_parent = target_parents.pop()
    parent[target_parent] = -2

    for i in range(N):
        if parent[i] == target_parent:
            parent[i] = -2
            target_parents.append(i)

# 제거되지 않은(부모 값이 -2가 아닌) 노드 중, 자신을 부모로 삼는 다른 노드가
# 하나도 존재하지 않으면 리프 노드임
count_leaf = 0
for target in range(N):
    if parent[target] == -2:
        continue

    is_leaf = True

    for i in range(N):
        if parent[i] == target:
            is_leaf = False
            break
    
    if is_leaf:
        count_leaf += 1

print(count_leaf)
