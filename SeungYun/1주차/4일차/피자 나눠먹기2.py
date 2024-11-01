def solution(n):
    piece = 6
    while not piece % n == 0:
        piece += 6
    return piece // 6
# 그냥 최소 공배수 구하는 문제인데 약간 브루트 포스 너낌으로 풀어봤습니다