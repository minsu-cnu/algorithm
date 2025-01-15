dividend_1, divisor_1 = map(int, input().split())
dividend_2, divisor_2 = map(int, input().split())

# 각 분수의 통분 후 분자
dividend_1_new = dividend_1 * divisor_2
dividend_2_new = dividend_2 * divisor_1

# 합한 후의 분자, 분모
dividend_new = dividend_1_new + dividend_2_new
divisor_new = divisor_1 * divisor_2

# 2부터, 분자or분모 아무거나의 제곱근까지 공약수인지 판별 후 계속 나눠주기기
for div in range(2, int(divisor_new ** 0.5)):
    while dividend_new % div == 0 and divisor_new % div == 0:
        dividend_new //= div
        divisor_new //= div

print(dividend_new, divisor_new)