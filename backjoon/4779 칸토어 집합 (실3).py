import sys
input = sys.stdin.readline

def cantoer(left_idx, right_idx, line):
    if left_idx == right_idx:
        return line[left_idx]

    split_size = (right_idx - left_idx + 1) // 3
    left_line = cantoer(left_idx, left_idx + split_size - 1, line)
    right_line = cantoer(right_idx - split_size + 1, right_idx, line)

    return left_line + " " * split_size + right_line

N = -1
while True:
    try:
        N = int(input().strip())
    except:
        break

    line = "-" * (3 ** N)
    print(cantoer(0, len(line) - 1, line))


