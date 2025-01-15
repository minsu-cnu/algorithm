N, B = map(int, input().split())
result_str = ''

while N > 0:
    rest = N % B
    N = N // B
    
    if 10 <= rest <= 35:
        result_str += chr(rest + 55)
    else:
        result_str += str(rest)

print(result_str[::-1])