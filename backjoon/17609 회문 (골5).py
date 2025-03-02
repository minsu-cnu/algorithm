import sys
input = sys.stdin.readline

def is_palindrome(string, left_idx, right_idx):
    while left_idx < right_idx:
        if string[left_idx] == string[right_idx]:
            left_idx += 1
            right_idx -= 1
        else:
            return False
    
    return True

def is_palindrome_with_cutting(string):
    left_idx = 0
    right_idx = len(string) - 1
    result = 0

    while left_idx < right_idx:
        if string[left_idx] == string[right_idx]:
            left_idx += 1
            right_idx -= 1
        else:
            is_pseudo = is_palindrome(string, left_idx + 1, right_idx) or is_palindrome(string, left_idx, right_idx - 1)
            if is_pseudo:
                result = 1
            else:
                result = 2
            
            break
    
    return result


T = int(input().rstrip())

for _ in range(T):
    string = input().rstrip()
    print(is_palindrome_with_cutting(string))
    