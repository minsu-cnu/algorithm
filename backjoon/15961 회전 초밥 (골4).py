import sys
from collections import deque
input = sys.stdin.readline

N, d, k, c = map(int, input().rstrip().split())
belt = [int(input().rstrip()) for _ in range(N)]
type_counts = [0] * (d + 1) # k개 후보 내의 idx번 초밥의 개수 기록 딕셔너리
type_counts[c] = 1 # 쿠폰 초밥 개수 1개 기록해두기

# 고정 크기 K 윈도우의 양쪽 투 포인터
left_idx = 0
right_idx = k - 1

result = 0
eat_types = 1 # k개 후보 내에서 먹은 가짓수를 기록하는 변수

# 최초 윈도우 내의 종류별 먹은 개수 딕셔너리와, 먹은 가짓수를 구하기
for num in belt[:k]:
    if type_counts[num] == 0:
        eat_types += 1
    
    type_counts[num] += 1

# 윈도우를 슬라이딩하면서 딕셔너리와 먹은 가짓수 변수를 갱신해나가기
while left_idx <= N - 1:
    result = max(result, eat_types)

    type_num = belt[left_idx]
    if type_counts[type_num] == 1:
        eat_types -= 1
    
    type_counts[type_num] -= 1
    
    left_idx += 1
    right_idx += 1

    # 원형 순환 구조임을 고려하여 right_idx 정제
    type_num = belt[right_idx if right_idx // N == 0 else right_idx % N]
    if type_counts[type_num] == 0:
        eat_types += 1
    
    type_counts[type_num] += 1

print(result)