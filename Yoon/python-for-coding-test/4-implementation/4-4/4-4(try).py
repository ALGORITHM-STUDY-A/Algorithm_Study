# 48분 소모 / 오답 / 이 코드는 단절된 공간에 0이 존재하면 무한루프에 빠진다 / 입력 예시일 때는 실행이 되지만 반례가 존재함.

n, m = map(int, input().split())

s_y, s_x, d = map(int, input().split())

data = [list(map(int, (input().split()))) for _ in range(n)]

count = 1   # 시작점 카운트
data[s_y][s_x] = -1 # 시작점 방문처리


def turn_left(d):   # 왼쪽으로 돌게 해주는 함수
    if d == 0:  # 북쪽은 -1 하면 음수가 되어서 이렇게 구현
        return 3    # 서쪽으로 이동
    else:
        return d-1  # 그 외에는 -1 진행


while any(0 in row for row in data):    # data의 한 행에 0이 있나 판별하는 부분 / 나의 방문처리 방식

    d = turn_left(d)    # 먼저 돌고

    # 밑에 4가지 조건문은 각 방향별로 이동을 구현했다
    if d == 0 and s_y - 1 >= 0 and data[s_y - 1][s_x] == 0:
        s_y += 1
        data[s_y][s_x] = -1
        count += 1

    elif d == 1 and s_x + 1 <= m - 1 and data[s_y][s_x + 1] == 0:
        s_x += 1
        data[s_y][s_x] = -1
        count += 1

    elif d == 2 and s_y + 1 <= n - 1 and data[s_y + 1][s_x] == 0:
        s_y += 1
        data[s_y][s_x] = -1
        count += 1

    elif d == 3 and s_x - 1 >= 0 and data[s_y][s_x - 1] == 0:
        s_x += 1
        data[s_y][s_x] = -1
        count += 1

print(count)
