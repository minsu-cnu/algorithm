import sys
input = sys.stdin.readline

def is_valid():
    for c in "ACGT":
        if ACGT_count[c] < ACGT_min[c]:
            return False
    
    return True

S, P = map(int, input().rstrip().split())
DNA = input().rstrip()
tmp = [*map(int, input().rstrip().split())]
ACGT_min = dict(zip(list("ACGT"), tmp))

left_idx = 0
right_idx = P - 1
ACGT_count = dict(zip(list("ACGT"), [0] * 4))

for idx in range(left_idx, right_idx + 1):
    ACGT_count[DNA[idx]] += 1

result = 0
while right_idx < S:
    if is_valid():
        result += 1
    
    ACGT_count[DNA[left_idx]] -= 1
    left_idx += 1
    
    right_idx += 1

    if right_idx < S:
        ACGT_count[DNA[right_idx]] += 1

print(result)