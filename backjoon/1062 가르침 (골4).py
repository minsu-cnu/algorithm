import sys
from itertools import combinations
input = sys.stdin.readline

def convert_word_to_bit(word):
    converted_bit = 0b0
    for c in word:
        converted_bit |= 1 << (ord(c) - 96)

    return converted_bit

def is_readable(word_bit, candidate_bit):
    return (word_bit | candidate_bit) <= candidate_bit

def solution(K, base_bit):
    if K < 5:
        return 0
    
    K_rest = K - 5
    result = 0

    for locs in combinations(set(range(1, 27)) - base_loc, K_rest):
        candidate_bit = base_bit
        
        for loc in locs:
            candidate_bit |= 1 << loc

        count = 0
        for word in words:
            word_bit = convert_word_to_bit(word)

            if is_readable(word_bit, candidate_bit):
                count += 1
        
        result = max(result, count)
    
    return result


N, K = map(int, input().rstrip().split())
words = [input().rstrip() for _ in range(N)]

base_bit = 0b0
base_loc = set()
for c in "antic":
    bit_loc = ord(c) - 96
    base_loc.add(bit_loc)
    base_bit |= 1 << bit_loc

print(solution(K, base_bit))