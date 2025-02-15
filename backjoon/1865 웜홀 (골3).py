import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    N, M, W = map(int, input().rstrip().split())
    edges = []

    for _ in range(M):
        S, E, T = map(int, input().rstrip().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    
    for _ in range(W):
        S, E, T = map(int, input().rstrip().split())
        edges.append((S, E, -T))

    # 최단 거리는 필요 없고 오직 음의 사이클이 있는지만 판단하면 되기 때문에,
    # costs는 임의의 값으로 모두 똑같이만 채워두면 된다.
    costs = [0] * (N + 1)
    result = False
    for step in range(N):
        for start, end, cost in edges:
            cal_cost = costs[start] + cost

            if cal_cost < costs[end]:
                costs[end] = cal_cost

                if step == N - 1:
                    result = True
    
    print("YES" if result else "NO")
