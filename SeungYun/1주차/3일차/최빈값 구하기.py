def solution(array):
    n = len(array)
    A = set(array)

    maxValue = -1 # max라 쓰긴 했는데 최빈값임
    maxCount = -1 # 최대 개수
    for i in A: #중복 제거한 배열 하나씩 꺼내서 반복
        count = 0
        for j in range(n):
            if i == array[j]:
                count += 1 # 같은 값이 있으면 +1
        if count > maxCount: # 최대 개수보다 큰 값이면 갱신
            maxCount = count
            maxValue = i
        elif count == maxCount: # 최대 개수와 같은 개수면 -1 이후 최대 개수보다 큰값이 나오면 다시 갱신됨
            maxValue = -1
    return maxValue
# 내가 좋아하는 브루트 포스 ㅎㅎ

