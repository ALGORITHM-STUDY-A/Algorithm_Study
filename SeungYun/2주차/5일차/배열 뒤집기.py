# 파이썬은 음수 인덱싱도 가능 인덱스가 0, 1, 2, 3이라면 각각 -4, -3, -2, -1
# 슬라이싱 기능도 제공 [start: end: step] start는 시작 요소, end는 끝요소 step은 인덱스를 얼마나 증가시킬지
# (start ~ end 직전 요소)
def solution(num_list):
    answer = num_list[::-1]
    return answer


def solution2(num_list):
    num_list.reverse()
    return num_list
