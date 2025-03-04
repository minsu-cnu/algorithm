import sys
input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
board = [input().rstrip() for _ in range(R)]
words = []

for row in range(R):
    row_word = ""
    for col in range(C):
        if board[row][col] == "#":
            if len(row_word) > 1:
                words.append(row_word)
            
            row_word = ""
        else:
            row_word += board[row][col]

    if len(row_word) > 1:
        words.append(row_word)

for col in range(C):
    col_word = ""
    for row in range(R):
        if board[row][col] == "#":
            if len(col_word) > 1:
                words.append(col_word)
            
            col_word = ""
        else:
            col_word += board[row][col]

    if len(col_word) > 1:
        words.append(col_word)


print(sorted(words)[0])