n = int(input())
x, y = 1, 1

plans = input().split()

# L,R,U,D 에 따라 각 행과 열이 움직이는 값들
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for plan in plans:  # 입력값들 차례대로 조회
    for i in range(len(move_types)):    # 미리 지정한 LRUD
        if plan == move_types[i]:
            nx = x + dx[i]  # L R U D 에 맞게 조율
            ny = y + dy[i]  # L R U D 에 맞게 조율

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue    # 만약 조율 이후 지도를 벗어나는 경우 무시

    x, y = nx, ny   # 조율 이후 지도 안에 있다면 해당 값 반영
