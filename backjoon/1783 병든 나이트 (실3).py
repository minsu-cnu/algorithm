import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 1행 : 결과값 1
# 2행 : 1~2열 1, 3~4열 2, 5~6열 3, 7열부터 4
# 3행부터 : 1열 1, 2열 2, 3열 3, 4열~6열 4, 7열부터 m-2 

result = 0

if N == 1:
    result = 1
elif N == 2:
    if 1 <= M <= 2:
        result = 1
    elif 3 <= M <= 4:
        result = 2
    elif 5 <= M <= 6:
        result = 3
    else:
        result = 4
else:
    result = M

    if 5 <= M <= 6:
        result = 4
    elif M >= 7:
        result = M - 2

print(result)