from itertools import combinations, product

L, C = map(int, input().split())
alphabets = [*map(str, input().split())]

# 알파벳 체계에서의 모든 모음과 자음 집합
vowels_all = set(["a", "e", "i", "o", "u"])
consonants_all = set([str(chr(i)) for i in range(97, 123)]) - vowels_all

# 주어진 문자들을 모음, 자음 그룹으로 분류
vowels = [item for item in alphabets if item in vowels_all]
consonants = [item for item in alphabets if item in consonants_all]

# 가능성 있는 암호 후보 리스트 (결과값)
secret_candidates = []

# 조건 상에서 최대로 사용 가능한 모음 개수
vowel_max = min(len(vowels), L - 2)

for vowel_count in range(1, vowel_max + 1):
    consonant_count = L - vowel_count

    # 정해진 모음, 자음 개수에 대해, 자모음 그룹 각각에서 가능한 모든 후보군(경우의 수)
    vowel_candidates = combinations(vowels, vowel_count)
    consonant_candidates = combinations(consonants, consonant_count)

    # 후보군끼리 합치고 정렬해서 가능성 있는 암호 구하기
    for vowel_candidate, consonant_candidate in product(vowel_candidates, consonant_candidates):
        secret_candidate = ''.join(sorted(vowel_candidate + consonant_candidate))
        secret_candidates.append(secret_candidate)

print(*sorted(secret_candidates), sep="\n")