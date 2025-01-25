import heapq

N = int(input())
hq = []
count = 0

for _ in range(N):
    card = int(input())
    heapq.heappush(hq, card)

while len(hq) > 1:
    card_1 = heapq.heappop(hq)
    card_2 = heapq.heappop(hq)
    card_sum = card_1 + card_2
    count += card_sum
    heapq.heappush(hq, card_sum)

print(count)
