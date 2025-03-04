import sys
input = sys.stdin.readline

N = int(input().rstrip())
result = []

for _ in range(N):
    string = input().rstrip()
    num_string = ""

    for char in string:
        if 48 <= ord(char) <= 57:
            num_string += char
        elif len(num_string) > 0:
                result.append(int(num_string))
                num_string = ""
    
    if len(num_string) > 0:
         result.append(int(num_string))
    
print(*sorted(result), sep = "\n")
