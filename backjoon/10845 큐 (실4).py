from collections import deque
import sys

# 그냥 input 쓰니까 TLE 뜸
# 앞으로도 걍 최적화 느낌으로 readline 써주자

N = int(sys.stdin.readline().strip())
dq = deque()

for _ in range(N):
    command_line = sys.stdin.readline().strip().split()
    command = command_line[0]

    if len(command_line) == 2:
        number = int(command_line[1])
    
    if command == "push":
        dq.append(number)
    elif command == "pop":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif command == "size":
        print(len(dq))
    elif command == "empty":
        print(1 if len(dq) == 0 else 0)
    elif command == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif command == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])