import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(origin, sub):
    root_origin = find(origin)
    root_sub = find(sub)

    if root_origin == root_sub:
        return False
    
    parent[root_origin] = root_sub
    return True

G = int(input().rstrip())
P = int(input().rstrip())

# idx번 게이트의 대체 게이트는 value번 게이트
# value번 게이트도 또 다른 대체 게이트가 있을 수 있음. 연쇄적임
parent = [g for g in range(G + 1)]
result = 0

for _ in range(P):
    g = int(input().rstrip())
    g_sub = find(g) # g번 게이트의 대체 게이트 (g번이 아직 가능하다면 g번일 수 있음)

    if g_sub == 0: # 대체 게이트가 0번이란 것은 도킹이 불가능하다는 것을 의미
        break

    # 대체 게이트 g_sub에 도킹했으니, 이제 g_sub 게이트의 대체 게이트는 g_sub-1 번 게이트임
    # 만약 g_sub-1번 게이트가 이미 사용되어 대체 게이트가 있다면, g_sub도 그걸 대체 게이트로 삼게됨(유니온 파인드 원리)
    union(g_sub, g_sub - 1)
    result += 1

print(result)