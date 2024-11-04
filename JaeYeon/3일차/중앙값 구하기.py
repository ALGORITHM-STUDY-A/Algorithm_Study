def solution(array):

    # 우선 배열을 정렬합니다
    array.sort()

    # 배열의 길이를 구하고
    n=len(array)
    # 그 길이를 2로 나눠서 몫을 반환합니다
    # 그 값이 중앙 인덱스가 됩니다
    mid=n//2

    # 그리고 그 중앙인덱스에 맞는 값을 반환합니다
    return array[mid]