import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    line = [*map(int, input().rstrip().split())]
    soldier_count = line[0]
    soldier_nums = line[1:]
    boundary = soldier_count / 2

    soldier_dict = defaultdict(int)
    for soldier_num in soldier_nums:
        soldier_dict[soldier_num] += 1
    
    result = "SYJKGW"
    for soldier_num, count in soldier_dict.items():
        if count > boundary:
            result = soldier_num
            break
    
    print(result)
