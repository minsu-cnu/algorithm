import sys, math
input = sys.stdin.readline

k = int(input().rstrip())

# 초기는 step 0인 것으로 정의
# k는 (step-1)**2 + 1 번째 문자부터 step**2 번째까지의 문자들 중에 하나의 위치임
step = math.ceil(math.log2(k))

def search_order(k, step):
    if step == 0:
        return "0"

    result = ""

    # step에 해당하는 현재 취급 범위를 절반으로 나눴을 때, 왼쪽 그룹의 가장 우측 문자
    end_in_left_group = 2 ** (step - 1)
    
    if k <= end_in_left_group: # 왼쪽 그룹이라면 범위만 왼쪽 그룹만큼으로 축소해주기
        result = search_order(k, step - 1)
    else: # 오른쪽 그룹이라면, 오른쪽 그룹에서와 똑같은 서수를 가진 왼쪽 그룹에서의 위치의 문자를 반전시켜 리턴
        k_convert_left_group = k - end_in_left_group
        result = "0" if search_order(k_convert_left_group, step - 1) == "1" else "1"
    
    return result

print(search_order(k, step))