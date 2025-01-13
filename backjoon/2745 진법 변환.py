N, B = map(str, input().split())
B = int(B)
N_decimal = 0
digit_iter = 0

for digit in N[::-1]:
    base_num = B ** digit_iter
    if 65 <= ord(digit) <= 90:
        N_decimal += base_num * (ord(digit) - 55)
    elif 48 <= ord(digit) <= 57:
        N_decimal += base_num * (ord(digit) - 48)
    digit_iter += 1

print(N_decimal)