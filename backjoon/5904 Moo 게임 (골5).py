import sys
input = sys.stdin.readline

# k : S(k) 에서의 k
# n : N을, 현재 S(k) 내에서의 서수로 치환한 값
# length : S(k)의 길이
def search_order(k, n, length):
    middle_group_size = k + 3
    side_group_size = (length - middle_group_size) // 2

    if n <= side_group_size:
        return search_order(k - 1, n, side_group_size)
    elif n == side_group_size + 1:
        return "m"
    elif n <= side_group_size + middle_group_size:
        return "o"
    else:
        return search_order(k - 1, n - (side_group_size + middle_group_size), side_group_size)


N = int(input().rstrip())
k, length = 0, 3

while N > length:
    k += 1
    length = length * 2 + (k + 3)

# 이 시점에서 N번째 글자는, S(k)를 구성하는 문자 중에 반드시 존재한다.
print(search_order(k, N, length))