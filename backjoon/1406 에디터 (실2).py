import sys

line = sys.stdin.readline().strip()
M = int(input())

# 덱(더블 링크드 리스트로 구현된 큐)과 리스트로는 중간 원소 삽입 및 삭제
# 시간복잡도가 높아서 TLE남
# 커서 개념을 고정시키고, 왼쪽과 오른쪽 부분을 따로 스택으로 두어,
# 커서의 이동, 중간 원소 삭제&삽입 개념을 O(1)로 수행
left_str = list(line)
right_str_reversed = [] # left와 맞닿은 부분은 right 스택의 가장 오른쪽 원소

for _ in range(M):
    command_line = sys.stdin.readline().strip().split()
    command = command_line[0]

    if command == "P":
        input_str = command_line[1]
    
    if command == "L":
        if len(left_str) > 0:
            right_str_reversed.append(left_str.pop())
    elif command == "D":
        if len(right_str_reversed) > 0:
            left_str.append(right_str_reversed.pop())
    elif command == "B":
        if len(left_str) > 0:
            left_str.pop()
    elif command == "P":
        left_str.append(input_str)
    

print(''.join(left_str) + ''.join(right_str_reversed[::-1]))
