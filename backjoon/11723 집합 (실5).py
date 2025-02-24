import sys
input = sys.stdin.readline

M = int(input().rstrip())
S = 0b0

for _ in range(M):
    line = input().rstrip().split()
    command = line[0]

    if command == "add":
        num = int(line[1])
        S |= (1 << num)
    elif command == "remove":
        num = int(line[1])
        S &= (~(1 << num))
    elif command == "check":
        num = int(line[1])
        print(1 if S & (1 << num) > 0 else 0)
    elif command == "toggle":
        num = int(line[1])
        S ^= (1 << num)
    elif command == "all":
        S = 0b111111111111111111111
    elif command == "empty":
        S = 0b0