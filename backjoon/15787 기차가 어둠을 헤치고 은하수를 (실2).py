import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
train_info = [0b0] * (N + 1)

for _ in range(M):
    line = [*map(int, input().rstrip().split())]
    command = line[0]
    train_num = line[1]

    if command == 1:
        passenger_num = line[2]
        train_info[train_num] |= (1 << passenger_num)
    elif command == 2:
        passenger_num = line[2]
        train_info[train_num] &= ~(1 << passenger_num)
    elif command == 3:
        train_info[train_num] = (train_info[train_num] << 1) & (~(1 << 21))
    elif command == 4:
        train_info[train_num] = (train_info[train_num] >> 1) & (~1)
        
result = 0
train_status = set()
for train_num in range(1, N + 1):
    if train_info[train_num] not in train_status:
        result += 1
        train_status.add(train_info[train_num])

print(result)