def solution(array):
    sortedArray = sorted(array) # 배열 정렬
    mid = len(array) // 2 # 배열 중앙 인덱스 값
    return sortedArray[mid]
