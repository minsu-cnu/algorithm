import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
dq = deque(range(1, N + 1))
result = []

while dq:
    for _ in range(K - 1):
        dq.append(dq.popleft())
    
    result.append(dq.popleft())

print("<" + ", ".join(map(str, result)) + ">")