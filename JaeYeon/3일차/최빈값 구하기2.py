from collections import Counter


def solution(array):
    # 각 요소의 출현 횟수를 세기
    counter = Counter(array)

    # 최빈값과 그 횟수 찾기
    max_count = max(counter.values())
    mode_candidates = [num for num, count in counter.items() if count == max_count]

    # 최빈값이 여러 개이면 -1 반환
    if len(mode_candidates) > 1:
        return -1
    else:
        return mode_candidates[0]


# 예시 실행
print(solution([1, 2, 2, 3, 3]))  # -1 (2와 3이 동일하게 최빈값)
print(solution([1, 1, 2, 2, 2, 3]))  # 2 (2가 최빈값)