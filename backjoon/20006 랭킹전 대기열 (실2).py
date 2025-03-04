import sys
input = sys.stdin.readline

p, m = map(int, input().rstrip().split())
rooms = [] # [[방 기준 레벨 or 시작 여부, [(레벨, 닉), (레벨, 닉), ...]], ...]

for _ in range(p):
    l, n = input().rstrip().split()
    l = int(l)

    is_entered = False
    for room_num in range(len(rooms)): # 생성 시간 순으로 방 순회
        room_level = rooms[room_num][0]

        # 시작한 방이 아니면서 입장 가능한 방일 때, 입장 시키기
        if room_level != -1 and room_level - 10 <= l <= room_level + 10:
            rooms[room_num][1].append((l, n))
            is_entered = True

            # 방이 가득찼다면 시작 처리
            if len(rooms[room_num][1]) == m:
                rooms[room_num][0] = -1
            
            break
    
    # 들어갈 방이 없으면 새로 만들기 (방 정원이 1명이라면, 방 생성과 동시에 즉시 시작 처리)
    if not is_entered:
        rooms.append([l if m > 1 else -1, [(l, n)]])

for room in rooms:
    room_info = "Started!\n" if room[0] == -1 else "Waiting!\n"

    for player in sorted(room[1], key = lambda x: x[1]):
        room_info += str(player[0]) + " " + str(player[1]) + "\n"
    
    print(room_info, end="")

