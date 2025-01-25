import sys

N = int(sys.stdin.readline().strip())
num_counts = {}

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    
    if num in num_counts:
        num_counts[num] += 1
    else :
        num_counts[num] = 1

num_counts_items = []
for num, count in num_counts.items():
    num_counts_items.append((count, num))

print(sorted(num_counts_items, key=lambda x:(-x[0], x[1]))[0][1])