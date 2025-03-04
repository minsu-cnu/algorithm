import sys
input = sys.stdin.readline

N, L, F = input().rstrip().split()
N = int(N)
L_to_min = int(L[:3]) * 24 * 60 + int(L[4:6]) * 60 + int(L[7:9])
F = int(F)
rental_infos = {} # key : object와 owner 문자열의 결합, value : 대여 일시를 분 단위로 환산한 값
result = {}

# key : n월, value : n-1월까지를 일수로 환산
# 해당 딕셔너리를 만드는 과정
month_to_min = {1: 0, 2: 31, 3: 28, 4: 31, 5: 30, 6: 31, 7: 30, 8: 31, 9: 31, 10: 30, 11: 31, 12: 30}

for month in range(2, 13):
    month_to_min[month] += month_to_min[month - 1]

for month in range(2, 13):
    month_to_min[month] *= 24 * 60

for _ in range(N):
    day, time, obj, owner = input().rstrip().split()

    # 대여 일시를 분 단위로 환산
    month = month_to_min[int(day[5:7])]
    day = int(day[8:10]) * 24 * 60
    hour = int(time[:2]) * 60
    minute = int(time[3:])

    rental_key = obj + owner
    rental_to_minute = month + day + hour + minute

    if rental_key in rental_infos: # 같은 object&owner에 대해 대여 기록이 존재(반납 시도임을 의미)
        rental_spending_minute = rental_to_minute - rental_infos[rental_key]
        late_minute = rental_spending_minute - L_to_min

        if late_minute > 0:
            if owner not in result:
                result[owner] = 0

            result[owner] += late_minute * F

        rental_infos.pop(rental_key)
    else:
        rental_infos[rental_key] = rental_to_minute

if len(result.keys()) != 0:
    for student, cost in sorted(result.items(), key=lambda x: x[0]):
        print(student, cost)
else:
    print(-1)
