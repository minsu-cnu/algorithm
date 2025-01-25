import sys, heapq
scan = sys.stdin.readline

N, K = map(int, scan().strip().split())

jewels = []

for _ in range(N):
    M, V = map(int, scan().strip().split())
    jewels.append((M, V))

# 보석 무게가 가벼운 것부터 pop해서 쓰기 위해 무게 기준 내림차순 정렬
jewels.sort(reverse=True, key=lambda x:x[0])

bags = []

for _ in range(K):
    C = int(scan().strip())
    bags.append(C)

# 가방 무게가 가벼운 것부터 pop해서 쓰기 위해 무게 기준 내림차순 정렬
bags.sort(reverse=True)

# 현재 단계의 가방에 넣을 수 있는 보석 후보군들 (가격 기준 우선순위 큐)
jewel_candidate = []

# 결과값
V_sum_max = 0

# 모든 가방에 보석 넣기 시도
while bags:
    # 남아있는 가용 가방 중 최소 용량 가방
    bag_weight = bags.pop()

    # 남아있는 모든 보석들에 대해, 가방에 넣을 수 있는 후보군인지 판별
    while jewels:
        jewel = jewels.pop()
        M, V = jewel

        if M <= bag_weight:
            heapq.heappush(jewel_candidate, -V)
        else:
            jewels.append(jewel)
            break
    
    if jewel_candidate:
        V_sum_max += -heapq.heappop(jewel_candidate)

print(V_sum_max)


