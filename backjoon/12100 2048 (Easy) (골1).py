import sys, copy
input = sys.stdin.readline

def move_4(board, move_count):
    if move_count == 5:
        max_num = 0

        for row in range(len(board)):
            max_num = max(max_num, max(board[row]))

        return max_num
    
    result = 0
    board_move = copy.deepcopy(board)
    board_absorption = [[False] * len(board_move) for _ in range(len(board_move))]

    # 위로 밀기
    for row in range(1, len(board_move)):
        for col in range(len(board_move)):
            target_item = board_move[row][col]

            if target_item == 0:
                continue

            for row_move in range(row - 1, -1, -1):
                comparison_target = board_move[row_move][col]
                is_absorption = board_absorption[row_move][col]
                
                if comparison_target == 0:
                    board_move[row_move][col] = target_item
                    board_move[row_move + 1][col] = 0
                elif target_item == comparison_target:
                    if not is_absorption:
                        board_move[row_move][col] = target_item * 2
                        board_move[row_move + 1][col] = 0
                        board_absorption[row_move][col] = True
                    
                    break
                else:
                    break
    
    result = max(result, move_4(board_move, move_count + 1))
    board_move = copy.deepcopy(board)
    board_absorption = [[False] * len(board_move) for _ in range(len(board_move))]

    # 아래로 밀기
    for row in range(len(board_move) - 2, -1, -1):
        for col in range(len(board_move)):
            target_item = board_move[row][col]

            if target_item == 0:
                continue

            for row_move in range(row + 1, len(board_move)):
                comparison_target = board_move[row_move][col]
                is_absorption = board_absorption[row_move][col]
                
                if comparison_target == 0:
                    board_move[row_move][col] = target_item
                    board_move[row_move - 1][col] = 0
                elif target_item == comparison_target:
                    if not is_absorption:
                        board_move[row_move][col] = target_item * 2
                        board_move[row_move - 1][col] = 0
                        board_absorption[row_move][col] = True
                    
                    break
                else:
                    break

    result = max(result, move_4(board_move, move_count + 1))
    board_move = copy.deepcopy(board)
    board_absorption = [[False] * len(board_move) for _ in range(len(board_move))]

    # 왼쪽으로 밀기
    for col in range(1, len(board_move)):
        for row in range(len(board_move)):
            target_item = board_move[row][col]

            if target_item == 0:
                continue

            for col_move in range(col - 1, -1, -1):
                comparison_target = board_move[row][col_move]
                is_absorption = board_absorption[row][col_move]
                
                if comparison_target == 0:
                    board_move[row][col_move] = target_item
                    board_move[row][col_move + 1] = 0
                elif target_item == comparison_target:
                    if not is_absorption:
                        board_move[row][col_move] = target_item * 2
                        board_move[row][col_move + 1] = 0
                        board_absorption[row][col_move] = True
                    
                    break
                else:
                    break

    result = max(result, move_4(board_move, move_count + 1))
    board_move = copy.deepcopy(board)
    board_absorption = [[False] * len(board_move) for _ in range(len(board_move))]

    # 오른쪽으로 밀기
    for col in range(len(board_move) - 2, -1, -1):
        for row in range(len(board_move)):
            target_item = board_move[row][col]

            if target_item == 0:
                continue

            for col_move in range(col + 1, len(board_move)):
                comparison_target = board_move[row][col_move]
                is_absorption = board_absorption[row][col_move]
                
                if comparison_target == 0:
                    board_move[row][col_move] = target_item
                    board_move[row][col_move - 1] = 0
                elif target_item == comparison_target:
                    if not is_absorption:
                        board_move[row][col_move] = target_item * 2
                        board_move[row][col_move - 1] = 0
                        board_absorption[row][col_move] = True
                    
                    break
                else:
                    break
    
    result = max(result, move_4(board_move, move_count + 1))
    return result

N = int(input().rstrip())
board = [[*map(int, input().rstrip().split())] for _ in range(N)]

print(move_4(board, 0))