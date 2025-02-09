# 1안
# S가 홀수라면, 홀수의 개수가 홀수개이면 된다.
# S가 짝수라면, 홀수의 개수가 짝수개이면 된다.

# 2안
# 일단 1부터 연속으로 다 채우기 직전까지 쭉 더해보기
# 그 때까지 더한 자연수 개수를 K개라고 하자
# 합을 K+1만큼 증가 <-> 자연수 개수 1개 증가 가능
# 그보다 적은 증가량은 자연수 개수 그대로 유지하면서 증가 가능
import sys
input = sys.stdin.readline

S = int(input().rstrip())
K = 0
cur_sum = 0

for num in range(1, 100000000):
    cur_sum += num

    if cur_sum > S:
        cur_sum -= num
        break    

    K = num

rest = S - cur_sum
while True:
    if rest < K + 1:
        break

    rest -= K + 1
    K += 1

print(K)