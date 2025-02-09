import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip())
times = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
times.sort(key=lambda x: (x[0], x[1]))
end_of_rooms = [0]

for start, end in times:
    if end_of_rooms[0] <= start:
        heapq.heappop(end_of_rooms)
    
    heapq.heappush(end_of_rooms, end)

print(len(end_of_rooms))