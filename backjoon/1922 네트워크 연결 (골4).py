import sys
input = sys.stdin.readline

def find(x):
    if parent[x] < 0:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return False
    
    if parent[root_x] < parent[root_y]:
        parent[root_y] = root_x
        parent[root_x] -= 1
    elif parent[root_x] > parent[root_y]:
        parent[root_x] = root_y
        parent[root_y] -= 1
    else:
        parent[root_x] = root_y
        parent[root_y] -= 1
    
    return True

N = int(input().rstrip())
edges = []

for _ in range(int(input().rstrip())):
    a, b, c = map(int, input().rstrip().split())

    if a != b:
        edges.append((c, a, b))

edges.sort()
parent = [-1] * (N + 1)
result = 0

for c, a, b in edges:
    if union(a, b):
        result += c

print(result)